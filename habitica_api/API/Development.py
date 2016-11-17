from .apicall import apiCall


@apiCall(request_type='post',
         resource='debug/add-hourglass')
def add_hourglass_to_user():
    pass


@apiCall(request_type='post',
         resource='debug/add-ten-gems')
def add_ten_gems_to_user():
    pass


@apiCall(request_type='post',
         resource='debug/quest-progress')
def accelerate_quest_progress():
    pass


@apiCall(request_type='post',
         resource='debug/modify-inventory')
def modify_user_inventory():
    pass


@apiCall(request_type='post',
         resource='debug/make-admin')
def make_admin():
    pass
