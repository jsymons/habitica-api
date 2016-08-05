import requests

class Task:

	DIFFICULTY = {0.1:'Trivial',1:'Easy',1.5:'Medium',2:'Hard'}

	def __init__(self,owner=None,id=None,title=None,notes=None,tags=None,difficulty=1.5,**kwargs):
		self.owner = owner
		self.id = id
		self.title = title
		self.notes = notes
		self.tags = tags
		self.difficulty = Task.DIFFICULTY[difficulty]

	def delete(self):
		request_url = 'https://habitica.com/api/v3/tasks/%s' % (self.id)
		r = requests.delete(request_url,headers=self.owner.credentials)
		self.owner.update_tasks()



