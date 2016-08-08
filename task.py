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

	def modify(self,data):
		modified_data = data.copy()
		if 'title' in modified_data.keys():
			modified_data['text'] = modified_data['title']
			modified_data.pop('title')
		if 'difficulty' in modified_data.keys():
			modified_data['priority'] = modified_data['difficulty']
			modified_data.pop('difficulty')
		if self.owner.h.modify_task(self.id,modified_data):
			self.owner.update_tasks()



