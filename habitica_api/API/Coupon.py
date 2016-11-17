from .apicall import apiCall


@apiCall(request_type='post',
         resource='coupons/generate/:event',
         containers=['url_var', 'params'])
def generate(event, count_):
    url_var = {'event': event}
    params = {'count': count_}


@apiCall(request_type='get',
         resource='coupons')
def get():
    pass


@apiCall(request_type='post',
         resource='coupons/enter/:code',
         containers=['url_var'])
def redeem(code):
    return {'code': code}


@apiCall(request_type='post',
         resource='coupons/validate/:code',
         containers=['url_var'])
def validate(code):
    return {'code': code}
