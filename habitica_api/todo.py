from .task import Task
from . import API


class ToDo(Task):

    @classmethod
    def new(cls, **kwargs):
        kwargs['type'] = 'todo'
        update = API.Task.new(kwargs)
        if update is not None:
            return cls(**update)
        else:
            return None


class ToDos(object):
    def __init__(self):
        data = API.Task.get_all(type_="todos")
        self.todos = []
        for todo in data:
            self.todos.append(ToDo(**todo))

    def __iter__(self):
        for todo in self.todos:
            yield todo
