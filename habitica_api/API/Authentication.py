from . import User


headers = {'content-type': 'application/json'}
logged_in = False


def login(username, password):
    global headers, logged_in
    auth = User.login(username, password)
    headers['x-api-user'] = auth['id']
    headers['x-api-key'] = auth['apiToken']
    logged_in = True


def logout():
    global headers, logged_in
    if logged_in:
        headers.pop('x-api-user')
        headers.pop('x-api-key')
        logged_in = False
