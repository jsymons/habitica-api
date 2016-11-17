from .apicall import apiCall


@apiCall(request_type='post',
         resource='groups',
         containers=['data'])
def create(group_data):
    return group_data


@apiCall(request_type='get',
         resource='groups/:groupId',
         containers=['url_var'])
def get(group_id):
    return {'groupId': group_id}


@apiCall(request_type='get',
         resource='groups',
         containers=['params'])
def get_groups_for_user(type_):
    return {'type': type_}


@apiCall(request_type='post',
         resource='groups/:groupId/invite',
         containers=['url_var', 'data'])
def invite_to_group(group_id, email=None, emails=None,
                    name=None, uuids=None):
    if not email and not emails and not uuids:
        raise ValueError('One of email, emails, or uuids must be given')
    url_var = {'groupId': group_id}
    data = {}
    if email:
        data['email'] = email
    if emails:
        data['emails'] = emails
    if uuids:
        data['uuids'] = uuids
    return url_var, data


@apiCall(request_type='post',
         resource='groups/:groupId/join',
         containers=['url_var'])
def join(group_id):
    return {'groupId': group_id}


@apiCall(request_type='post',
         resource='groups/:groupId/leave',
         containers=['url_var', 'params'])
def leave(group_id, keep='keep-all'):
    url_var = {'groupId': group_id}
    params = {'keep': keep}
    return url_var, params


@apiCall(request_type='post',
         resource='groups/:groupId/reject',
         containers=['url_var'])
def reject_invite(group_id):
    return {'groupId': group_id}


@apiCall(request_type='post',
         resource='groups/:groupId/removeMember/:memberId',
         containers=['url_var', 'params'])
def remove_group_member(group_id, member_id, message):
    url_var = {'groupId': group_id,
               'memberId': member_id}
    params = {'message': message}
    return url_var, params


@apiCall(request_type='put',
         resource='groups/:groupId',
         containers=['url_var', 'data'])
def update(group_id, group_updates):
    url_var = {'groupId': group_id}
    data = group_updates
    return url_var, data
