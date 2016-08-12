from .task import Task
from .connection import Connection

class Habit(Task):

	def __init__(self,up=None,down=None,**kwargs):
		super().__init__(**kwargs)
		self.up = up
		self.down = down

	def update(self,**kwargs):
		updated_task = super().update(**kwargs)
		if updated_task is not None:
			self.up = updated_task.pop('up', None)
			self.down = updated_task.pop('down', None)

	@classmethod
	def add(cls,title,notes=None,tags=None,difficulty=None,up=None,down=None,owner=None):
		new_habit = {'text':title,'type':'habit'}
		if notes is not None:
			new_habit['notes'] = notes
		if tags is not None:
			new_habit['tags'] = tags
		if difficulty is not None:
			new_habit['priority'] = difficulty
		if up is not None:
			new_habit['up'] = up
		if down is not None:
			new_habit['down'] = down

		update = Connection.active.add_task(new_habit)

		if update['success']:
			return cls(owner=owner,**update['data'])
		else:
			return None