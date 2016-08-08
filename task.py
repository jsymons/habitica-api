import requests

class Task:

	DIFFICULTY = {0.1:'Trivial',1:'Easy',1.5:'Medium',2:'Hard'}
	DAILY = 'dailys'
	TODO = 'todos'
	HABIT = 'habits'

	def __init__(self,owner=None,id=None,title=None,notes=None,tags=None,difficulty=1.5,type=None,**kwargs):
		self.owner = owner
		self.id = id
		if 'text' in kwargs.keys():
			self.title = kwargs['text']
		else:
			self.title = title
		self.notes = notes
		self.tags = tags
		if 'priority' in kwargs.keys():
			self.difficulty = kwargs['priority']
		else:
			self.difficulty = difficulty
		self.type = type

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

	def add_to_checklist(self,text):
		if self.type in ['daily','todo']:
			checklist_item = {'text':text}
			if self.owner.h.add_to_checklist(self.id,checklist_item):
				self.owner.update_tasks()

	def delete_from_checklist(self,checklist_item_id):
		if self.type in ['daily','todo']:
			if self.owner.h.delete_from_checklist(self.id,checklist_item_id):
				self.owner.update_tasks()

	def edit_checklist(self,id,text):
		if self.type in ['daily', 'todo']:
			updated_checklist_item = {'text':text}
			if self.owner.h.edit_checklist(self.id,id,updated_checklist_item):
				self.owner.update_tasks()


