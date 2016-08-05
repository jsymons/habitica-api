import requests
from .task import Task
from .habit import Habit
from .daily import Daily
from .todo import ToDo

class NewLogin:

	def __init__(self):
		self.login_status = False
		self.credentials = {}

	def login(self,username,password):
		credentials = {'username': username, 'password': password}
		r = requests.post('https://habitica.com/api/v3/user/auth/local/login', data=credentials)
		if r.status_code == 200:
			self.credentials['x-api-user'] = r.json()['data']['id']
			self.credentials['x-api-key'] = r.json()['data']['apiToken']
			self.login_status = True

	def update_status(self):
		r = requests.get('https://habitica.com/api/v3/user', headers=self.credentials)
		if r.json()['success']:
			self.profile = r.json()['data']
			return True
		else:
			return False


	def add_habit(self,title,notes=None,tags=None,difficulty=None,up=None,down=None):
		new_habit = {'text':title,'type':'habit'}
		if notes:
			new_habit['notes'] = notes
		if tags:
			new_habit['tags'] = tags
		if difficulty:
			new_habit['priority'] = difficulty
		if up is not None:
			new_habit['up'] = 'true' if up else 'false'
		if down is not None:
			new_habit['down'] = 'true' if down else 'false'
		r = requests.post('https://habitica.com/api/v3/tasks/user', headers=self.credentials, data=new_habit)
		self.update_tasks(task_type='habits')


	def add_daily(self,title):
		new_daily = {'text':title,'type':'daily'}
		r = requests.post('https://habitica.com/api/v3/tasks/user', headers=self.credentials, data=new_daily)
		self.update_tasks(task_type='dailies')



	def add_todo(self,title):
		new_todo = {'text':title,'type':'todo'}
		r = requests.post('https://habitica.com/api/v3/tasks/user', headers=self.credentials, data=new_todo)
		self.update_tasks(task_type='todos')

	def update_tasks(self,task_type=None):
		if task_type is None:
			r = requests.get('https://habitica.com/api/v3/tasks/user', headers=self.credentials)
		elif task_type == 'dailies':
			r = requests.get('https://habitica.com/api/v3/tasks/user', headers=self.credentials, params={'type':'dailys'})
		else:
			r = requests.get('https://habitica.com/api/v3/tasks/user', headers=self.credentials, params={'type':task_type})
		if r.json()['success']:
			if task_type == 'habits':
				self.habits = []
			elif task_type == 'dailies':
				self.dailies = []
			elif task_type == 'todos':
				self.todos == []
			else:
				self.habits = []
				self.dailies = []
				self.todos = []
			for task in r.json()['data']:
				if task['type'] == 'habit':
					habit = Habit.data_import(task)
					habit.owner = self
					self.habits.append(habit)
				elif task['type'] == 'daily':
					daily = Daily.data_import(task)
					daily.owner = self
					self.dailies.append(daily)
				elif task['type'] == 'todo':
					todo = ToDo.data_import(task)
					todo.owner = self
					self.todos.append(todo)





