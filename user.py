import requests

class NewLogin:

	def __init__(self):
		self.login_status = False
		self.userid = ''
		self.apiToken = ''

	def login(self,username,password):
		credentials = {'username': username, 'password': password}
		r = requests.post('https://habitica.com/api/v3/user/auth/local/login', data=credentials)
		if r.status_code == 200:
			self.userid = r.json()['data']['id']
			self.apiToken = r.json()['data']['apiToken']
			self.login_status = True

