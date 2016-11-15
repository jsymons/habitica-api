class Item():

	def __init__(self,**kwargs):
		self.klass = kwargs.get('klass',None)
		self.con = kwargs.get('con',None)
		self.int = kwargs.get('int',None)
		self.per = kwargs.get('per',None)
		self.str = kwargs.get('str',None)
		self.notes = kwargs.get('notes',None)
		self.key = kwargs.get('key',None)
		self.set = kwargs.get('set',None)
		self.text = kwargs.get('text',None)
		self.type = kwargs.get('type',None)
		self.value = kwargs.get('value',None)
