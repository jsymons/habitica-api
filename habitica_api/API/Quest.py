from .apicall import apiCall


@apiCall(request_type='post',
         resource='groups/:groupId/quests/abort',
         containers=['url_var'])
def abort(group_id):
    return {'groupId': group_id}


@apiCall(request_type='post',
         resource='groups/:groupId/quests/accept',
         containers=['url_var'])
def accept(group_id):
    return {'groupId': group_id}


@apiCall(request_type='post',
         resource='groups/:groupId/quests/cancel',
         containers=['url_var'])
def cancel_nonactive_quest(group_id):
    return {'groupId': group_id}


@apiCall(request_type='post',
         resource='groups/:groupId/quests/force-start',
         containers=['url_var'])
def force_start(group_id):
    return {'groupId': group_id}


@apiCall(request_type='post',
         resource='groups/:groupId/quests/invite',
         containers=['url_var', 'data'])
def invite_group(group_id, quest_key):
    url_var = {'groupId': group_id}
    data = {'questKey': quest_key}
    return url_var, data


@apiCall(request_type='post',
         resource='groups/:groupId/quests/leave',
         containers=['url_var'])
def leave(group_id):
    return {'groupId': group_id}


@apiCall(request_type='post',
         resource='groups/:groupId/quests/reject',
         containers=['url_var'])
def reject(group_id):
    return {'groupId': group_id}
