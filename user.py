import requests
import json
from .task import Task
from .habit import Habit
from .daily import Daily
from .todo import ToDo
from .tag import Tag
from .connection import Connection

class User():

	def __init__(self):
		pass
		

	def update_status(self):
		status = Connection.active.get_status()
		if status is not None:
			self.profile = status
			return True
		else:
			return False
	
	def add_habit(self,**kwargs):
		new_habit = Habit.add(owner=self,**kwargs)
		if new_habit is not None:
			self.habits.append(new_habit)
		
		

	def add_daily(self,**kwargs):
		new_daily = Daily.add(owner=self,**kwargs)
		if new_daily is not None:
			self.dailies.append(new_daily)
		


	def add_todo(self,**kwargs):
		new_todo = ToDo.add(owner=self,**kwargs)
		if new_todo is not None:
			self.todos.append(new_todo)

	def update_tasks(self,task_type=None):
		if task_type is not None:
			tasks = Connection.active.get_tasks(task_type)
		else:
			tasks = Connection.active.get_tasks()

		if tasks is not None:
			if task_type == Task.HABIT:
				self.habits = []
			elif task_type == Task.DAILY:
				self.dailies = []
			elif task_type == Task.TODO:
				self.todos = []
			else:
				self.habits = []
				self.dailies = []
				self.todos = []

			for task in tasks:
				if task['type'] == 'habit':
					self.habits.append(Habit(owner=self,**task))
				elif task['type'] == 'daily':
					self.dailies.append(Daily(owner=self,**task))
				elif task['type'] == 'todo':
					self.todos.append(ToDo(owner=self,**task))

	def update_tags(self):
		tags = Connection.active.get_tags()
		if tags is not None:
			self.tags = []
			for tag in tags:
				self.tags.append(Tag(**tag))





