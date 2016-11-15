import requests
import json
from functools import wraps

BASE_URL = "https://habitica.com/api/v3/"


class Authentication(object):
    headers = {'content-type': 'application/json'}
    logged_in = False

    @classmethod
    def login(cls, username, password):
        credentials = {'username': username, 'password': password}
        login_url = 'user/auth/local/login'
        r = requests.post(BASE_URL + login_url,
                          headers=self.headers,
                          data=json.dumps(credentials))
        if r.status_code == 200:
            auth = r.json()
            self.headers['x-api-user'] = auth['data']['id']
            self.headers['x-api-key'] = auth['data']['apiToken']
            self.login_status = True


class NotLoggedInError(Exception):
    pass


class TransactionError(Exception):
    pass


class apiAccessor(object):
    def __init__(self, override_url=None):
        self.override_url = override_url

    def _data_handler(self, f, *args, **kwargs):
        if not Authentication.logged_in:
            raise NotLoggedInError()
        # get api root name from parent class of method
        #
        # args[0] is the parent class since only decorating
        # class methods
        root = args[0].__name__
        # f.__name__.replace converts method name to proper url
        if self.override_url is None:
            endpoint = f.__name__.replace('_', '-')
        else:
            endpoint = self.override_url
        url = BASE_URL + root + '/' + endpoint
        headers = Authentication.headers
        data = f(*args, **kwargs)
        return url, headers, data


class apiPut(apiAccessor):

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            url, headers, data = self._data_handler(f)
            r = requests.put(url=url, headers=headers, data=json.dumps(data))
            if r.status_code == 200:
                return r.json()
            else:
                raise TransactionError(r)
    return wrapper


class apiPost(apiAccessor):

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            url, headers, data = self._data_handler(f)
            r = requests.post(url=url, headers=headers, data=json.dumps(data))
            if r.status_code == 200:
                return r.json()
            else:
                raise TransactionError(r)
    return wrapper


class apiDelete(apiAccessor):

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            url, headers, _ = self._data_handler(f)
            r = requests.delete(url=url, headers=headers)
            if r.status_code == 200:
                return r.json()
            else:
                raise TransactionError(r)


class apiGet(apiAccessor):

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            url, headers, params = self._data_handler(f, *args, *kwargs)
            r = requests.get(url=url, headers=headers, params=params)
        if r.status_code == 200:
            return r.json()
        else:
            raise TransactionError(r)


class User(object):
    url = BASE_URL + 'user/'

    @classmethod
    @apiPost
    def allocate(cls, stat='str'):
        return {'stat': stat}

    @classmethod
    @apiPost
    def block(cls, uuid):
        return {'uuid': uuid}

    @classmethod
    @apiPost
    def buy_health_potion(cls):
        pass

    @classmethod
    @apiPost
    def buy_mystery_set(cls, key):
        return {'key': key}

    @classmethod
    @apiPost
    def buy_gear(cls, key):
        return {'key': key}

    @classmethod
    @apiPost
    def buy_quest(cls, key):
        return {'key': key}

    @classmethod
    @apiPost
    def buy_armoire(cls):
        pass

    @classmethod
    @apiPost
    def buy(cls, key):
        return {'key': key}

    @classmethod
    @apiPost
    def buy_special_spell(cls, key):
        return {'key': key}

    @classmethod
    @apiPost(override_url='class/cast/')
    def class_cast(cls, spell_id, target_id):
        return {'spellId': spell_id,
                'targetId': target_id}

    @classmethod
    @apiPost
    def change_class(cls, _class):
        return {'class': _class}

    @classmethod
    @apiDelete(override_url='messages')
    def delete_messages(cls, message_id=None):
        if message_id is not None:
            return {'id': message_id}

    @classmethod
    @apiPost
    def disable_classes(cls):
        pass

    @classmethod
    @apiPost
    def equip(cls, _type, key):
        return {'type': _type,
                'key': key}

    @classmethod
    @apiPost
    def feed(cls, pet, food):
        return {'pet': pet,
                'food': food}

    @classmethod
    @apiGet(override_url='')
    def profile(cls):
        pass

    @classmethod
    @apiGet(override_url='inventory/buy')
    def available_for_purchase(cls):
        pass

    @classmethod
    @apiPost
    def hatch(cls, egg, hatching_potion):
        return {'egg': egg,
                'hatchingPotion': hatching_potion}

    @classmethod
    @apiPost
    def sleep(cls):
        pass

    @classmethod
    @apiPost
    def mark_pms_read(cls):
        pass

    @classmethod
    @apiPost
    def open_mystery_item(cls):
        pass

    @classmethod
    @apiPost
    def purchase(cls, _type, key):
        return {'type': _type,
                'key': key}

    @classmethod
    @apiPost
    def purchase_hourglass(cls, _type, key):
        return {'type': _type,
                'key': key}

    @classmethod
    @apiPost
    def read_card(cls, card_type):
        return {'cardType': card_type}

    @classmethod
    @apiPost
    def release_mounts(cls):
        pass

    @classmethod
    @apiPost
    def release_both(cls):
        pass

    @classmethod
    @apiPost
    def reroll(cls):
        pass

    @classmethod
    @apiPost
    def reset_password(cls, email):
        return {'email': email}

    @classmethod
    @apiPost
    def reset(cls):
        pass

    @classmethod
    @apiPost
    def revive(cls):
        pass

    @classmethod
    @apiPost
    def sell(cls, _type, key):
        return {'type': _type,
                'key': key}

    @classmethod
    @apiPost
    def unlock(cls, path):
        return {'path': path}

    @classmethod
    @apiPost
    def rebirth(cls):
        pass