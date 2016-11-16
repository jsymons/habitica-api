import requests
import json

JSON_HEADERS = {'content-type': 'application/json'}
BASE_URL = "https://habitica.com/api/v3/"

class Connection():

	active = None
	user = None

	def __init__(self):
		self.headers = JSON_HEADERS.copy()
		self.login_status = False
		
	def post(self,url,data=None):
		if not self.login_status:
			raise NotLoggedInException()
		if data is not None:
			r = requests.post(BASE_URL+url, headers=self.headers, data=json.dumps(data))
		else:
			r = requests.post(BASE_URL+url, headers=self.headers)
		return r.json()

	def get(self,url,params=None):
		if not self.login_status:
			raise NotLoggedInException()
		if params is not None:
			r = requests.get(BASE_URL+url, headers=self.headers,params=params)
		else:
			r = requests.get(BASE_URL+url, headers=self.headers)
		return r.json()

	def delete(self,url):
		if not self.login_status:
			raise NotLoggedInException()
		r = requests.delete(BASE_URL+url,headers=self.headers)
		return r.json()

	def put(self,url,data):
		if not self.login_status:
			raise NotLoggedInException()
		r = requests.put(BASE_URL+url, headers=self.headers, data=json.dumps(data))
		return r.json()


	def login(self,username,password):
		credentials = {'username': username, 'password': password}
		login_url = 'user/auth/local/login'
		r = requests.post(BASE_URL+login_url, headers=self.headers, data=json.dumps(credentials)).json()
		if r['success']:
			self.headers['x-api-user'] = r['data']['id']
			self.headers['x-api-key'] = r['data']['apiToken']
			self.login_status = True

		Connection.active = self

	def get_status(self):
		r = self.get('user')
		if r['success']:
			return r['data']
		else:
			return None

	def add_task(self,data):
		return self.post('tasks/user',data)
		

	def get_tasks(self,task_type=None):
		if task_type:
			r = self.get('tasks/user',params={'type':task_type})
		else:
			r = self.get('tasks/user')
		if r['success']:
			return r['data']
		else:
			return None

	def delete_task(self,id):
		request_url = 'tasks/%s' % (id)
		r = self.delete(request_url)
		return r['success']

	def modify_task(self,id,data):
		request_url = 'tasks/%s' % (id)
		return self.put(request_url,data)
		

	def add_to_checklist(self,id,data):
		request_url = 'tasks/%s/checklist' % (id)
		return self.post(request_url,data)
		

	def delete_from_checklist(self,id,checklist_item_id):
		request_url = 'tasks/%s/checklist/%s' % (id,checklist_item_id)
		return self.delete(request_url)
		

	def edit_checklist(self,id,checklist_item_id,data):
		request_url = 'tasks/%s/checklist/%s' % (id,checklist_item_id)
		return self.put(request_url,data)
		

	def score_task(self,id,direction='up'):
		request_url = 'tasks/%s/score/%s' % (id,direction)
		r = self.post(request_url)
		return r['success']

	def score_checklist(self,id,check_id):
		request_url = 'tasks/%s/checklist/%s/score' %(id,check_id)
		return self.post(request_url)
		

	def get_task(self,id):
		request_url = 'tasks/%s' % (id)
		r = self.get(request_url)
		if r['success']:
			return r['data']
		else:
			return None

	def get_tags(self):
		request_url = 'tags'
		r = self.get(request_url)
		if r['success']:
			return r['data']
		else:
			return None

	def add_tag(self,data):
		request_url = 'tags'
		r = self.post(request_url,data)
		if r['success']:
			return r['data']
		else:
			return None

	def delete_tag(self,id):
		request_url = 'tags/%s' % (id)
		r = self.delete(request_url)
		return r['success']

	def rename_tag(self,id,data):
		request_url = 'tags/%s' % (id)
		r = self.put(request_url,data)
		return r['success']

	def add_tag_to_task(self,taskid,tagid):
		request_url = 'tasks/%s/tags/%s' % (taskid,tagid)
		r = self.post(request_url)
		if r['success']:
			return r['data']
		else:
			return None

	def remove_tag_from_task(self,taskid,tagid):
		request_url = 'tasks/%s/tags/%s' % (taskid,tagid)
		r = self.delete(request_url)
		if r['success']:
			return r['data']
		else:
			return None

	def buy_health_potion(self):
		request_url = 'user/buy-health-potion'
		r = self.post(request_url)
		if r['success']:
			return r['data']
		else:
			return None

	def buy_item(self,key):
		request_url = 'user/buy-gear/%s' % (key)
		r = self.post(request_url)
		if r['success']:
			return r['data']['items']
		else:
			return None

	def get_buy_list(self):
		request_url = 'user/inventory/buy'
		r = self.get(request_url)
		if r['success']:
			return r['data']
		else:
			return None


class NotLoggedInException(Exception):
	pass
