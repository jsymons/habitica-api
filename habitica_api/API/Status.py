from .apicall import apiCall


@apiCall(request_type='get',
         resource='status',
         requires_authentication=False)
def get():
    pass
