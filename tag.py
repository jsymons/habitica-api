from .connection import Connection

class Tag():

	all = []

	def __init__(self,id=None,name=None,tasks=[]):
		self.id = id
		self.name=name
		self.tasks=tasks
		Tag.all.append(self)

	@classmethod
	def update_all(cls):
		tags = Connection.active.get_tags()
		if tags is not None:
			Tag.all = []
			for tag in tags:
				Tag(**tag)