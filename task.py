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
			self.update()

	def add_to_checklist(self,text):
		if self.type in ['daily','todo']:
			checklist_item = {'text':text}
			if self.owner.h.add_to_checklist(self.id,checklist_item):
				self.update()

	def delete_from_checklist(self,checklist_item_id):
		if self.type in ['daily','todo']:
			if self.owner.h.delete_from_checklist(self.id,checklist_item_id):
				self.update()

	def edit_checklist(self,id,text):
		if self.type in ['daily', 'todo']:
			updated_checklist_item = {'text':text}
			if self.owner.h.edit_checklist(self.id,id,updated_checklist_item):
				self.update()

	def score(self,direction='up'):
		if self.owner.h.score_task(self.id,direction):
			if self.type != 'habit':
				self.update()

	def score_checklist(self,check_id):
		if self.type in ['daily', 'todo']:
			if self.owner.h.score_checklist(self.id,check_id):
				self.update()


	def update(self):
		updated_task = self.owner.h.get_task(self.id)
		if updated_task is not None:
			self.title = updated_task.pop('text',None)
			self.notes = updated_task.pop('notes',None)
			self.tags = updated_task.pop('tags',None)
			self.difficulty = updated_task.pop('priority',None)
			return updated_task
		else:
			return None


