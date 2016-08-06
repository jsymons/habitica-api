import requests

class Task:

	DIFFICULTY = {0.1:'Trivial',1:'Easy',1.5:'Medium',2:'Hard'}
	DAILY = 'dailys'
	TODO = 'todos'
	HABIT = 'habits'

	def __init__(self,owner=None,id=None,title=None,notes=None,tags=None,difficulty=1.5,**kwargs):
		self.owner = owner
		self.id = id
		self.title = title
		self.notes = notes
		self.tags = tags
		self.difficulty = difficulty

	def delete(self):
		if self.owner.h.delete_task(self.id):
			self.owner.update_tasks()



