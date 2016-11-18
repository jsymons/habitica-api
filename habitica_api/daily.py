from .task import Task
from . import API


class Daily(Task):

    # Notes:
    # frequency indicated whether it is a days of the week
    # daily('weekly') or an every x day weekly('daily')

    # This determines if we should be looking at repeat(days
    # of the week) or everyX(every x days) to see if the task
    # is active
    @classmethod
    def new(cls, **kwargs):
        kwargs['type'] = 'daily'
        update = API.Task.new(kwargs)
        if update is not None:
            return cls(**update)
        else:
            return None


class Dailys(object):
    def __init__(self):
        data = API.Task.get_all(type_='dailys')
        self.dailys = []
        for d in data:
            self.dailys.append(Daily(**d))

    def __iter__(self):
        for d in self.dailys:
            yield d

    def __len__(self):
        return len(self.dailys)
