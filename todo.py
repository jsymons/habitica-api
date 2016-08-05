from .task import Task

class ToDo(Task):

	def __init__(self,checklist=None,completed=False,due_date=None,**kwargs):
		super().__init__(**kwargs)
		self.checklist = checklist
		self.completed = completed
		self.due_date = due_date

	@classmethod
	def data_import(cls,data):
		new_todo = cls(
			id=data['id'],
			title=data['text'],
			notes=data['notes'],
			tags=data['tags'],
			difficulty=data['priority']
			)
		new_todo.checklist = data['checklist']
		new_todo.completed = data['completed']
		if 'date' in data.keys():
			new_todo.due_date = data['date']
		return new_todo
