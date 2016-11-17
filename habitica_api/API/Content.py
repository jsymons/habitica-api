from .apicall import apiCall


@apiCall(request_type='get',
         resource='content',
         containers=['params'])
def get_all(language=None):
    if language:
        return {'language': language}
