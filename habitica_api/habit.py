from .task import Task
from . import API


class Habit(Task):

    @classmethod
    def new(cls, **kwargs):
        kwargs['type'] = 'habit'
        update = API.Task.new(kwargs)
        if update is not None:
            return cls(**update)
        else:
            return None


class Habits(object):
    def __init__(self):
        data = API.Task.get_all(type_="habits")
        self.habits = []
        for hab in data:
            self.habits.append(Habit(**hab))

    def __iter__(self):
        for hab in self.habits:
            yield hab
