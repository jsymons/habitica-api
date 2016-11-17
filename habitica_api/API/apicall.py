import requests
import json
from functools import wraps

from . import Authentication
from .config import BASE_URL


class NotLoggedInError(Exception):
    pass


class TransactionError(Exception):
    pass


def apiCall(request_type=None, resource=None,
            requires_authentication=True, containers=[]):
    request_types = {'get': requests.get,
                     'delete': requests.delete,
                     'post': requests.post,
                     'put': requests.put}
    valid_containers = ['url_var', 'params', 'data']

    def wrap(f):
        print(f.__name__)
        if request_type not in request_types:
            raise ValueError('Invalid request type: {}'.format(request_type))
        for t in containers:
            if t not in valid_containers:
                raise ValueError('Invalid data type: {}'.format(t))

        @wraps(f)
        def data_handler(*args, **kwargs):
            if requires_authentication is True and \
               Authentication.logged_in is False:
                raise NotLoggedInError()

            request_data = {}
            request_data['headers'] = Authentication.headers
            input_data = f(*args, **kwargs)
            res = resource

            def container_handler(container, c_data):
                nonlocal res
                if container == 'url_var':
                    for v in c_data:
                        if ':' in res:
                            res = res.replace(':' + v, c_data[v])
                if container == 'params':
                    request_data['params'] = c_data
                if container == 'data':
                    request_data['data'] = json.dumps(c_data)

            if len(containers) == 1:
                container_handler(containers[0], input_data)
            elif len(containers) > 1:
                for i, t in enumerate(containers):
                    container_handler(t, input_data[i])

            request_data['url'] = BASE_URL + res
            r = request_types[request_type](**request_data)
            if r.status_code in [200, 201]:
                return r.json().get('data', r.json())
            else:
                print('Status code: {}'.format(r.status_code))
                for rd in request_data:
                    print('{}:{}'.format(rd, request_data[rd]))
                raise TransactionError(r.json())

        return data_handler
    return wrap
