import requests

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

