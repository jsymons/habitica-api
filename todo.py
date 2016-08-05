import requests
from .task import Task

class ToDo(Task):

	def __init__(self):
		self.checklist = []
		self.completed = False

	def delete(self):
		request_url = 'https://habitica.com/api/v3/tasks/%s' % (self._id)
		r = requests.delete(request_url,headers=self.owner.credentials)
		self.owner.update_todos()