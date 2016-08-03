import requests
from .task import Task

class Habit(Task):

	def __init__(self):
		super().__init__()
		self.up = False
		self.down = True

	def delete(self):
		request_url = 'https://habitica.com/api/v3/tasks/%s' % (self._id)
		r = requests.delete(request_url,headers=self.owner.credentials)
		self.owner.update_habits()

