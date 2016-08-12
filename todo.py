from .task import Task
from .connection import Connection

class ToDo(Task):

	def __init__(self,checklist=None,completed=False,due_date=None,**kwargs):
		super().__init__(**kwargs)
		self.checklist = checklist
		self.completed = completed
		if 'date' in kwargs.keys():
			self.due_date = kwargs['date']
		else:
			self.due_date = due_date

	def update(self,**kwargs):
		updated_task = super().update(**kwargs)
		if updated_task is not None:
			self.checklist = updated_task.pop('checklist',None)
			self.completed = updated_task.pop('completed',None)
			self.due_date = updated_task.pop('date',None)

	@classmethod
	def add(cls,title,notes=None,date=None,difficulty=None,owner=None):
		new_todo = {'text':title,'type':'todo'}
		if notes:
			new_todo['notes'] = notes
		if date:
			new_todo['date'] = date
		if difficulty:
			new_todo['priority'] = difficulty

		update = Connection.active.add_task(new_todo)

		if update['success']:
			return cls(owner=owner,**update['data'])
		else:
			return None