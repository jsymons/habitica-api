from .task import Task
from .connection import Connection

class Habit(Task):

	all = []

	def __init__(self,up=None,down=None,**kwargs):
		super().__init__(**kwargs)
		self.up = up
		self.down = down
		Habit.all.append(self)

	def update(self,**kwargs):
		updated_task = super().update(**kwargs)
		if updated_task is not None:
			self.up = updated_task.pop('up', None)
			self.down = updated_task.pop('down', None)

	def delete(self):
		if super().delete():
			Habit.update_all()

	@classmethod
	def add(cls,title,notes=None,tags=None,difficulty=None,up=None,down=None):
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
			cls(**update['data'])
			return True
		else:
			return False

	@classmethod
	def update_all(cls):
		task_type = 'habits'
		habits = Connection.active.get_tasks(task_type)
		if habits is not None:
			Habit.all = []
			for habit in habits:
				Habit(**habit)
