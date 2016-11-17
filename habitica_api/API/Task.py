from .apicall import apiCall


@apiCall(request_type='post',
         resource='tasks/:taskId/tags/:tagId',
         containers=['url_var'])
def add_tag(task_id, tag_id):
    return {'taskId': task_id,
            'tagId': tag_id}


@apiCall(request_type='post',
         resource='tasks/:taskId/checklist',
         containers=['url_var', 'data'])
def add_to_checklist(task_id, text):
    url_var = {'taskId': task_id}
    data = {'text': text}
    return url_var, data


@apiCall(request_type='post',
         resource='tasks/:taskId/approve/:userId',
         containers=['url_var'])
def approve_user_assigned_to_group_task(task_id, user_id):
    return {'taskId': task_id,
            'userId': user_id}


@apiCall(request_type='post',
         resource='tasks/:taskId/assign/:userId',
         containers=['url_var'])
def assign_user_to_group_task(task_id, user_id):
    return {'taskId': task_id,
            'userId': user_id}


@apiCall(request_type='post',
         resource='tasks/challenge/:challengeId',
         containers=['url_var', 'data'])
def new_challenge_task(challenge_id, tasks):
    url_var = {'challengeId': challenge}
    data = tasks
    return url_var, tasks


@apiCall(request_type='post',
         resource='tasks/user',
         containers=['data'])
def new(task_data):
    return task_data


@apiCall(request_type='delete',
         resource='tasks/:taskId',
         containers=['url_var'])
def delete(task_id):
    return {'taskId': task_id}


@apiCall(request_type='post',
         resource='tasks/clearCompletedTodos')
def clear_completed_todos():
    pass


@apiCall(request_type='get',
         resource='tasks/challenge/:challengeId',
         containers=['url_var', 'params'])
def get_challenge_tasks(challenge_id, type_=None):
    url_var = {'challengeId': challenge_id}
    params = {}
    if type_:
        params['type'] = type_
    return url_var, params


@apiCall(request_type='get',
         resource='tasks/:taskId',
         containers=['url_var'])
def get(task_id):
    return {'taskId': task_id}


@apiCall(request_type='get',
         resource='tasks/user',
         containers=['params'])
def get_all(type_=None):
    if type_:
        return {'type': type_}


@apiCall(request_type='post',
         resource='tasks/:taskId/move/to/:position',
         containers=['url_var'])
def move(task_id, position):
    return {'taskId': task_id,
            'position': position}


@apiCall(request_type='delete',
         resource='tasks/:taskId/checklist/:itemId',
         containers=['url_var'])
def delete_from_checklist(task_id, item_id):
    return {'taskId': task_id,
            'itemId': item_id}


@apiCall(request_type='delete',
         resource='tasks/:taskId/tags/:tagId',
         containers=['url_var'])
def remove_tag(task_id, tag_id):
    return {'taskId': task_id,
            'tagId': tag_id}


@apiCall(request_type='post',
         resource='tasks/:taskId/checklist/:itemId/score',
         containers=['url_var'])
def score_checklist_item(task_id, item_id):
    return {'taskId': task_id,
            'itemId': item_id}


@apiCall(request_type='post',
         resource='tasks/:taskId/score/:direction',
         containers=['url_var'])
def score(task_id, direction='up'):
    return {'taskId': task_id,
            'direction': direction}


@apiCall(request_type='post',
         resource='tasks/:taskId/unassign/:userId',
         containers=['url_var'])
def unassign_user_from_group_task(task_id, user_id):
    return {'taskId': task_id,
            'userId': user_id}


@apiCall(request_type='post',
         resource='tasks/unlink-one/:taskId',
         containers=['url_var', 'params'])
def unlink_from_challenge(task_id, keep):
    url_var = {'taskId': task_id}
    params = {'keep': keep}
    return url_var, params


@apiCall(request_type='post',
         resource='tasks/unlink-all/:challengeId',
         containers=['url_var', 'params'])
def unlink_all_from_challenge(challenge_id, keep):
    url_var = {'challengeId': challenge_id}
    params = {'keep': keep}
    return url_var, params


@apiCall(request_type='put',
         resource='tasks/:taskId/checklist/:itemId',
         containers=['url_var', 'data'])
def update_checklist_item(task_id, item_id, text):
    url_var = {'taskId': task_id,
               'itemId': item_id}
    data = {'text': text}
    return url_var, data


@apiCall(request_type='put',
         resource='tasks/:taskId',
         containers=['url_var', 'data'])
def update(task_id, task_updates):
    url_var = {'taskId': task_id}
    data = task_updates
    return url_var, data
