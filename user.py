import requests
import json
from .task import Task
from .habit import Habit
from .daily import Daily
from .todo import ToDo
from .tag import Tag
from .connection import Connection

class User():

	active = None

	def __init__(self):
		User.active = self
		

	def update_status(self):
		status = Connection.active.get_status()
		if status is not None:
			self.profile = status
			self.hp = status['stats']['hp']
			self.maxhp = status['stats']['maxHealth']
			self.mp = status['stats']['mp']
			self.maxmp = status['stats']['maxMP']
			self.xp = status['stats']['exp']
			self.xp_to_level = status['stats']['toNextLevel']
			return True
		else:
			return False
	
