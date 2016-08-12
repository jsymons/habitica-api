from .connection import Connection

class Tag():

	def __init__(self,id=None,name=None,tasks=[]):
		self.id = id
		self.name=name
		self.tasks=tasks