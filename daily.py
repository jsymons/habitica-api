import requests
from .task import Task

class Daily(Task):

	def __init__(self):
		super().__init__()
		self.checklist = []
		self.completed = False
		self.streak = 0
		self.repeat = {}
		self.everyX = 0
		self.frequency = ""

	def delete(self):
		request_url = 'https://habitica.com/api/v3/tasks/%s' % (self._id)
		r = requests.delete(request_url,headers=self.owner.credentials)
		self.owner.update_dailies()