from .task import Task

class ToDo(Task):

	def __init__(self,checklist=None,completed=False,due_date=None,**kwargs):
		super().__init__(**kwargs)
		self.checklist = checklist
		self.completed = completed
		if 'date' in kwargs.keys():
			self.due_date = kwargs['date']
		else:
			self.due_date = due_date

