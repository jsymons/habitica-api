from .apicall import apiCall


@apiCall(request_type='post',
         resource='groups/:groupId/chat/:chatId/clearflags',
         containers=['url_var'])
def clear_flags(group_id, chat_id):
    return {'groupId': group_id,
            'chatId': chat_id}


@apiCall(request_type='delete',
         resource='groups/:groupId/chat/:chatId',
         containers=['url_var', 'params'])
def delete_chat_message(previous_message, group_id, chat_id):
    url_var = {'groupId': group_id,
               'chatId': chat_id}
    params = {'previousMsg': previous_message}
    return url_var, params


@apiCall(request_type='post',
         resource='groups/:groupId/chat/:chatId/flag',
         containers=['url_var'])
def flag_chat_message(group_id, chat_id):
    return {'groupId': group_id,
            'chatId': chat_id}


@apiCall(request_type='get',
         resource='groups/:groupId/chat',
         containers=['url_var'])
def get_messages(group_id):
    return {'groupId': group_id}


@apiCall(request_type='post',
         resource='groups/:groupId/chat/:chatId/like',
         containers=['url_var'])
def like_message(group_id, chat_id):
    return {'groupId': group_id,
            'chatId': chat_id}


@apiCall(request_type='post',
         resource='groups/:groupId/chat/seen',
         containers=['url_var'])
def mark_all_messages_from_group_read(group_id):
    return {'groupId': group_id}


@apiCall(request_type='post',
         resource='groups/:groupId/chat',
         containers=['url_var', 'data', 'params'])
def post_message(group_id, message, previous_message=None):
    url_var = {'groupId': group_id}
    data = {'message': message}
    if previous_message:
        params = {'previousMsg': previous_message}
    else:
        params = None
    return url_var, data, params
