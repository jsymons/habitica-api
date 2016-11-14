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
				cls(**tag)

	@classmethod
	def add(cls,name):
		data = {}
		data['name'] = name
		new_tag = Connection.active.add_tag(data)
		if new_tag is not None:
			return cls(**new_tag)
		else:
			return None

	def delete(self):
		if Connection.active.delete_tag(self.id):
			for tag in [tag for tag in Tag.all if tag.id == self.id]:
				Tag.all.remove(tag)

	def rename(self,new_name):
		data = {}
		data['name'] = new_name
		if Connection.active.rename_tag(self.id,data):
			self.name = new_name
			return True
		else:
			return False
