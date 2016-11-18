import requests
from . import API


def updates_task(f):
    def wrapper(self, *args, **kwargs):
        update = f(self, *args, **kwargs)
        self._import(**update)
    return wrapper


def manually_update_task(f):
    def wrapper(self, *args, **kwargs):
        f(self, *args, **kwargs)
        self._import(**API.Task.get(self.id))
    return wrapper


class Task(object):
    DIFFICULTY = {0.1: 'Trivial',
                  1: 'Easy',
                  1.5: 'Medium',
                  2: 'Hard'}

    def __init__(self, **kwargs):
        self._import(**kwargs)

    def delete(self):
        API.Task.delete(self.id)

    @updates_task
    def modify(self, data):
        return API.Task.update(self.id, data)

    @updates_task
    def add_to_checklist(self, text):
        return API.Task.add_to_checklist(self.id, text)

    @updates_task
    def delete_from_checklist(self, check_id):
        return API.Task.delete_from_checklist(self.id, check_id)

    @updates_task
    def update_checklist_item(self, id, text):
        return API.Task.update_checklist_item(self.id, id, text)

    @manually_update_task
    def score(self, direction='up'):
        API.Task.score(self.id, direction)

    @updates_task
    def score_checklist_item(self, check_id):
        return API.Task.score_checklist_item(self.id, check_id)

    def _import(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])