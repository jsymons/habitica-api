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
			return True
		else:
			return False
	
