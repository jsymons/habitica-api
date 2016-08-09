import requests
import json
from .task import Task
from .habit import Habit
from .daily import Daily
from .todo import ToDo

class User():

	def __init__(self,habitica_connection):
		self.h = habitica_connection

	def update_status(self):
		status = self.h.get_status()
		if status is not None:
			self.profile = status
			return True
		else:
			return False
	
	def add_habit(self,title,notes=None,tags=None,difficulty=None,up=None,down=None):
		new_habit = {'text':title,'type':'habit'}
		if notes is not None:
			new_habit['notes'] = notes
		if tags is not None:
			new_habit['tags'] = tags
		if difficulty is not None:
			new_habit['priority'] = difficulty
		if up is not None:
			new_habit['up'] = up
		if down is not None:
			new_habit['down'] = down

		update = self.h.add_task(new_habit)

		if update['success']:
			self.habits.append(Habit(owner=self,**update['data']))
		

	def add_daily(self,title,notes=None,tags=None,difficulty=None,repeat=None,everyX=None,frequency=None):
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

		update = self.h.add_task(new_daily)

		if update['success']:
			self.dailies.append(Daily(owner=self,**update['data']))
		


	def add_todo(self,title,notes=None,date=None,difficulty=None):
		new_todo = {'text':title,'type':'todo'}
		if notes:
			new_todo['notes'] = notes
		if date:
			new_todo['date'] = date
		if difficulty:
			new_todo['priority'] = difficulty

		update = self.h.add_task(new_todo)

		if update['success']:
			self.todos.append(ToDo(owner=self,**update['data']))

	def update_tasks(self,task_type=None):
		if task_type is not None:
			tasks = self.h.get_tasks(task_type)
		else:
			tasks = self.h.get_tasks()

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
					habit = Habit(owner=self,**task)
					self.habits.append(habit)
				elif task['type'] == 'daily':
					daily = Daily(owner=self,**task)
					self.dailies.append(daily)
				elif task['type'] == 'todo':
					todo = ToDo(owner=self,**task)
					self.todos.append(todo)





