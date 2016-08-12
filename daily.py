from .task import Task
from .connection import Connection

class Daily(Task):

# Notes:
# frequency indicated whether it is a days of the week
# daily('weekly') or an every x day weekly('daily')

# This determines if we should be looking at repeat(days
# of the week) or everyX(every x days) to see if the task
# is active


	def __init__(
		self,
		checklist=None,
		completed=False,
		streak=None,
		repeat=None,
		everyX=None,
		frequency=None,
		**kwargs
		):
		super().__init__(**kwargs)
		self.checklist = checklist
		self.completed = completed
		self.streak = streak
		self.repeat = repeat
		self.everyX = everyX
		self.frequency = frequency

	def update(self,**kwargs):
		updated_task = super().update(**kwargs)
		if updated_task is not None:
			self.checklist = updated_task.pop('checklist',None)
			self.completed = updated_task.pop('completed',None)
			self.streak = updated_task.pop('streak',None)
			self.repeat = updated_task.pop('repeat',None)
			self.everyX = updated_task.pop('everyX',None)
			self.frequency = updated_task.pop('frequency',None)

	@classmethod
	def add(cls,title,notes=None,tags=None,difficulty=None,repeat=None,everyX=None,frequency=None,owner=None):
		new_daily = {'text':title,'type':'daily'}
		if notes:
			new_daily['notes'] = notes
		if tags:
			new_daily['tags'] = tags
		if difficulty:
			new_daily['priority'] = difficulty
		if repeat:
			new_daily['repeat'] = repeat
		if everyX:
			new_daily['everyX'] = everyX
		if frequency:
			new_daily['frequency'] = frequency

		update = Connection.active.add_task(new_daily)

		if update['success']:
			return cls(owner=owner,**update['data'])
		else:
			return None