import requests
import json
from .task import Task
from .habit import Habit
from .daily import Daily
from .todo import ToDo
from .tag import Tag
from .connection import Connection
from .item import Item

class User():

	active = None

	def __init__(self):
		User.active = self
		self.buy_list = []
		self.inventory = {}
		Connection.user = self
		self.update_status()
		

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
			self.update_inventory(status['items'])
			return True
		else:
			return False
		

	def buy_health_potion(self):
		statsblock = Connection.active.buy_health_potion()
		if statsblock:
			self.hp = statsblock['hp']
			self.gp = statsblock['gp']

	def buy_item(self,key):
		items = Connection.active.buy_item(key)
		if items:
			self.update_inventory(items)
			self.update_status()

	def get_buy_list(self):
		buylist = Connection.active.get_buy_list()
		if buylist:
			for item in buylist:
				self.buy_list.append(Item(**item))

	def update_inventory(self,data):
		self.inventory['mounts'] = data['mounts']
		self.inventory['food'] = data['food']
		self.inventory['eggs'] = data['eggs']
		self.inventory['gear'] = data['gear']
		self.inventory['hatching_potions'] = data['hatchingPotions']
		self.inventory['pets'] = data['pets']
		self.inventory['quests'] = data['quests']
		self.inventory['special'] = data['special']



	
