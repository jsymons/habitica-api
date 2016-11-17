from .apicall import apiCall


@apiCall(request_type='post',
         resource='tags',
         containers=['data'])
def create(tag):
    return tag


@apiCall(request_type='delete',
         resource='tag/:tagId',
         containers=['url_var'])
def delete(tag_id):
    return {'tagId': tag_id}


@apiCall(request_type='get',
         resource='tags/:tagId',
         containers=['url_var'])
def get(tag_id):
    return {'tagId': tag_id}


@apiCall(request_type='get',
         resource='tags')
def get_all():
    pass


@apiCall(request_type='post',
         resource='reorder-tags',
         containers=['data'])
def reorder(tag_id, to):
    return {'tagId': tag_id,
            'to': to}


@apiCall(request_type='put',
         resource='tag/:tagId',
         containers=['url_var', 'data'])
def update(tag_id, tag_updates):
    url_var = {'tagId': tag_id}
    data = tag_updates
    return url_var, data
