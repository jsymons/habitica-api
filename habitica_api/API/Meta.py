from .apicall import apiCall


@apiCall(request_type='get',
         resource='models/:model/paths',
         requires_authentication=False,
         containers=['url_var'])
def get_paths_for_model(model):
    return {'model': model}
