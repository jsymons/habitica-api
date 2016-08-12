from .task import Task
from .connection import Connection

class ToDo(Task):

	all = []

	def __init__(self,checklist=None,completed=False,due_date=None,**kwargs):
		super().__init__(**kwargs)
		self.checklist = checklist
		self.completed = completed
		if 'date' in kwargs.keys():
			self.due_date = kwargs['date']
		else:
			self.due_date = due_date
		ToDo.all.append(self)

	def update(self,**kwargs):
		updated_task = super().update(**kwargs)
		if updated_task is not None:
			self.checklist = updated_task.pop('checklist',None)
			self.completed = updated_task.pop('completed',None)
			self.due_date = updated_task.pop('date',None)

	def delete(self):
		if super().delete():
			ToDo.update_all()

	@classmethod
	def add(cls,title,notes=None,date=None,difficulty=None):
		new_todo = {'text':title,'type':'todo'}
		if notes:
			new_todo['notes'] = notes
		if date:
			new_todo['date'] = date
		if difficulty:
			new_todo['priority'] = difficulty

		update = Connection.active.add_task(new_todo)

		if update['success']:
			cls(**update['data'])
			return True
		else:
			return False

	@classmethod
	def update_all(cls):
		task_type = 'todos'
		todos = Connection.active.get_tasks(task_type)
		if todos is not None:
			ToDo.all = []
			for todo in todos:
				ToDo(**todo)