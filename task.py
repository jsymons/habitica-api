import requests
from .connection import Connection

class Task:

	DIFFICULTY = {0.1:'Trivial',1:'Easy',1.5:'Medium',2:'Hard'}
	DAILY = 'dailys'
	TODO = 'todos'
	HABIT = 'habits'

	def __init__(self,id=None,title=None,notes=None,tags=None,difficulty=1.5,type=None,**kwargs):
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
		if Connection.active.delete_task(self.id):
			return True
		else:
			return False

	def modify(self,data):
		modified_data = data.copy()
		if 'title' in modified_data.keys():
			modified_data['text'] = modified_data['title']
			modified_data.pop('title')
		if 'difficulty' in modified_data.keys():
			modified_data['priority'] = modified_data['difficulty']
			modified_data.pop('difficulty')
		update = Connection.active.modify_task(self.id,modified_data)
		if update['success']:
			self.update(updated_task=update['data'])

	def add_to_checklist(self,text):
		if self.type in ['daily','todo']:
			checklist_item = {'text':text}
			update = Connection.active.add_to_checklist(self.id,checklist_item)
			if update['success']:
				self.update(updated_task=update['data'])

	def delete_from_checklist(self,checklist_item_id):
		if self.type in ['daily','todo']:
			update = Connection.active.delete_from_checklist(self.id,checklist_item_id)
			if update['success']:
				self.update(updated_task=update['data'])

	def edit_checklist(self,id,text):
		if self.type in ['daily', 'todo']:
			updated_checklist_item = {'text':text}
			update = Connection.active.edit_checklist(self.id,id,updated_checklist_item)
			if update['success']:
				self.update(updated_task=update['data'])

	def score(self,direction='up'):
		if Connection.active.score_task(self.id,direction):
			if self.type != 'habit':
				self.update()

	def score_checklist(self,check_id):
		if self.type in ['daily', 'todo']:
			update = Connection.active.score_checklist(self.id,check_id)
			if update['success']:
				self.update(updated_task=update['data'])


	def update(self,updated_task=None):
		if updated_task is None:
			updated_task = Connection.active.get_task(self.id)
		
		self.title = updated_task.pop('text',None)
		self.notes = updated_task.pop('notes',None)
		self.tags = updated_task.pop('tags',None)
		self.difficulty = updated_task.pop('priority',None)
		return updated_task

	def add_tag(self,tag):
		self.update(updated_task=Connection.active.add_tag_to_task(self.id,tag.id))

	def remove_tag(self,tag):
		self.update(updated_task=Connection.active.remove_tag_from_task(self.id,tag.id))
		
			


