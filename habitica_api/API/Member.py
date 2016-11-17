from .apicall import apiCall


@apiCall(request_type='get',
         resource='challenges/:challengeId/members/:memberId',
         containers=['url_var'])
def get_challenge_member_progress(challenge_id, member_id):
    return {'challengeId': challenge_id,
            'memberId': member_id}


@apiCall(request_type='get',
         resource='members/:memberId',
         containers=['url_var'])
def get_member_profile(member_id):
    return {'memberId': member_id}


@apiCall(request_type='get',
         resource='groups/:groupId/invites',
         containers=['url_var', 'params'])
def get_invites_for_group(group_id, last_id=None):
    url_var = {'groupId': group_id}
    params = {}
    if last_id:
        params = {'lastId': last_id}
    return url_var, params


@apiCall(request_type='get',
         resource='challenges/:challengeId/members',
         containers=['url_var', 'params'])
def get_challenge_members(challenge_id, last_id=None):
    url_var = {'challengeId': challenge_id}
    params = {}
    if last_id:
        params = {'lastId': last_id}
    return url_var, params


@apiCall(request_type='get',
         resource='groups/:groupId/members',
         containers=['url_var', 'params'])
def get_group_members(group_id, last_id=None,
                      include_all_public_fields=None):
    url_var = {'groupId': group_id}
    params = {}
    if last_id:
        params['lastId'] = last_id
    # only available when fetching party
    if include_all_public_fields is not None:
        params['includeAllPublicFields': include_all_public_fields]
    return url_var, params


@apiCall(request_type='post',
         resource='members/transfer-gems',
         containers=['data'])
def transfer_gems(message, to_user, gem_amount):
    return {'message': message,
            'toUserId': to_user,
            'gemAmount': gem_amount}


@apiCall(request_type='post',
         resource='members/send-private-message',
         containers=['data'])
def send_private_message(message, to_user):
    return {'message': message,
            'toUserId': to_user}
