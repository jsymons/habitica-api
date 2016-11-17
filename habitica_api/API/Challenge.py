from .apicall import apiCall


@apiCall(request_type='post',
         resource='challenges',
         containers=['data'])
def create_challenge(challenge):
    return challenge


@apiCall(request_type='delete',
         resource='challenges/:challengeId',
         containers=['url_var'])
def delete_challenge(challenge_id):
    return {'challengeId': challenge_id}


@apiCall(request_type='get',
         resource='challenges/:challengeId/export/csv',
         containers=['url_var'])
def export_challenge_to_csv(challenge_id):
    return {'challengeId': challenge_id}


@apiCall(request_type='get',
         resource='challenges/:challengeId',
         containers=['url_var'])
def get_challenge(challenge_id):
    return {'challengeId': challenge_id}


@apiCall(request_type='get',
         resource='challanges/groups/:groupId',
         containers=['url_var'])
def get_challenges_for_group(group_id):
    return {'groupId': group_id}


@apiCall(request_type='get',
         resource='challenges/user')
def get_challenges_for_user():
    pass


@apiCall(request_type='post',
         resource='challenges/:challengeId/join',
         containers=['url_var'])
def join_challenge(challenge_id):
    return {'challengeId': challenge_id}


@apiCall(request_type='post',
         resource='challenges/:challengeId/leave',
         containers=['url_var'])
def leave_challenge(challenge_id):
    return {'challengeId': challenge_id}


@apiCall(request_type='post',
         resource='challenges/:challengeId/selectWinner/:winnerId',
         containers=['url_var'])
def select_winner_for_challenge(challenge_id, winner_id):
    return {'challengeId': challenge_id,
            'winnerId': winner_id}


@apiCall(request_type='put',
         resource='challenges/:challengeId',
         containers=['url_var', 'data'])
def update_challenge(challenge_id, challenge_updates):
    url_var = {'challengeId': challenge_id}
    data = challenge_updates
    return url_var, data
