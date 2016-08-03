class Task:

	DIFFICULTY = {0.1:'Trivial',1:'Easy',1.5:'Medium',2:'Hard'}

	def __init__(self):
		self.owner = None
		self._id = ""
		self.title = ""
		self.notes = ""
		self.tags = []
		self.difficulty = ""



