from .task import Task

class Habit(Task):

	def __init__(self,up=None,down=None,**kwargs):
		super().__init__(**kwargs)
		self.up = up
		self.down = down

