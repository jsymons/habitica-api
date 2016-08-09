from .task import Task

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