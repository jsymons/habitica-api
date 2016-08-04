import requests
from .task import Task
from .habit import Habit
from .daily import Daily

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

	def update_habits(self):
		r = requests.get('https://habitica.com/api/v3/tasks/user', headers=self.credentials, params={'type':'habits'})
		if r.json()['success']:
			self.habits = []
			for task in r.json()['data']:
				habit = Habit()
				habit.owner = self
				habit._id = task['_id']
				habit.title = task['text']
				habit.notes = task['notes']
				habit.tags = task['tags']
				habit.difficulty = Task.DIFFICULTY[task['priority']]
				habit.up = task['up']
				habit.down = task['down']
				self.habits.append(habit)

	def add_habit(self,title):
		new_habit = {'text':title,'type':'habit'}
		r = requests.post('https://habitica.com/api/v3/tasks/user', headers=self.credentials, data=new_habit)
		self.update_habits()

	def update_dailies(self):
		r = requests.get('https://habitica.com/api/v3/tasks/user', headers=self.credentials, params={'type':'dailys'})
		if r.json()['success']:
			self.dailies = []
			for task in r.json()['data']:
				daily = Daily()
				daily.owner = self
				daily._id = task['_id']
				daily.title = task['text']
				daily.notes = task['notes']
				daily.tags = task['tags']
				daily.difficulty = Task.DIFFICULTY[task['priority']]
				daily.checklist = task['checklist']
				daily.completed = task['completed']
				daily.streak = task['streak']
				daily.repeat = task['repeat']
				daily.everyX = task['everyX']
				daily.frequency = task['frequency']
				self.dailies.append(daily)

	def add_daily(self,title):
		new_daily = {'text':title,'type':'daily'}
		r = requests.post('https://habitica.com/api/v3/tasks/user', headers=self.credentials, data=new_daily)
		self.update_dailies()


