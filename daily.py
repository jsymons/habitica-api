from .task import Task

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

	@classmethod
	def data_import(cls,data):
		new_daily = cls(
			id=data['id'],
			title=data['text'],
			notes=data['notes'],
			tags=data['tags'],
			difficulty=data['priority']
			)
		new_daily.checklist = data['checklist']
		new_daily.completed = data['completed']
		new_daily.streak = data['streak']
		new_daily.repeat = data['repeat']
		new_daily.everyX = data['everyX']
		new_daily.frequency = data['frequency']
		return new_daily


