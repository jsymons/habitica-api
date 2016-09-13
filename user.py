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
		self.update_status()
		Connection.user = self
		

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
			self.gp = status['stats']['gp']
			return True
		else:
			return False
		

	def buy_health_potion(self):
		statsblock = Connection.active.buy_health_potion()
		if statsblock:
			self.hp = statsblock['hp']
			self.gp = statsblock['gp']

	
