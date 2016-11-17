from .apicall import apiCall


@apiCall(request_type='get',
         resource='hall/heroes')
def get_heroes():
    pass


@apiCall(request_type='get',
         resource='hall/patrons',
         containers=['params'])
def get_patrons(page=0):
    return {'page': page}


@apiCall(request_type='get',
         resource='hall/heroes/:heroId',
         containers=['url_var'])
def get_hero(hero_id):
    return {'heroId': hero_id}


@apiCall(request_type='put',
         resource='hall/heroes/:heroId',
         containers=['url_var', 'data'])
def update_hero(hero_id, hero_updates):
    url_var = {'heroId': hero_id}
    data = hero_updates
    return url_var, data
