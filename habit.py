from .task import Task

class Habit(Task):

	def __init__(self,up=False,down=False,**kwargs):
		super().__init__(**kwargs)
		self.up = up
		self.down = down

	@classmethod
	def data_import(cls,data):
		new_habit = cls(
			id=data['id'],
			title=data['text'],
			notes=data['notes'],
			tags=data['tags'],
			difficulty=data['priority']
			)
		new_habit.up = data['up']
		new_habit.down = data['down']
		return new_habit