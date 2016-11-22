import requests
from . import API
from . import User


def updates_task(f):
    def wrapper(self, *args, **kwargs):
        update = f(self, *args, **kwargs)
        self._import(**update)
    return wrapper


def returns_updated_stats(f):
    def wrapper(self, *args, **kwargs):
        stats = f(self, *args, **kwargs)
        stats.pop('delta')
        stats.pop('_tmp')
        User._update_stats(stats)
        #manually update task
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

    @returns_updated_stats
    def score(self, direction='up'):
        return API.Task.score(self.id, direction)

    @updates_task
    def score_checklist_item(self, check_id):
        return API.Task.score_checklist_item(self.id, check_id)

    @updates_task
    def add_tag(self, tag):
        return API.Task.add_tag(self.id, tag.id)

    @updates_task
    def remove_tag(self, tag):
        return API.Task.remove_tag(self.id, tag.id)

    def _import(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])