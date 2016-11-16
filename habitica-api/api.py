import requests
import json
from functools import wraps
import weakref

BASE_URL = "https://habitica.com/api/v3/"


class Authentication(object):
    headers = {'content-type': 'application/json'}
    logged_in = False

    @classmethod
    def login(cls, username, password):
        credentials = {'username': username, 'password': password}
        login_url = 'user/auth/local/login'
        r = requests.post(BASE_URL + login_url,
                          headers=self.headers,
                          data=json.dumps(credentials))
        if r.status_code == 200:
            auth = r.json()
            self.headers['x-api-user'] = auth['data']['id']
            self.headers['x-api-key'] = auth['data']['apiToken']
            self.login_status = True

    @classmethod
    def register_new_user(cls, username, email, password, confirm_password):
        registration_details = {'username': username,
                                'email': email,
                                'password': password,
                                'confirmPassword': confirm_password
                                }
        register_url = 'user/auth/local/register'
        r = requests.post(BASE_URL + register_url,
                          headers=self.headers,
                          data=json.dumps(registration_details))
        if r.status_code == 200:
            return r.json()
        else:
            raise TransactionError(r)

    @classmethod
    def logout(cls):
        if logged_in:
            self.headers.pop('x-api-user')
            self.headers.pop('x-api-key')
            self.logged_in = False


class NotLoggedInError(Exception):
    pass


class TransactionError(Exception):
    pass


class apiCall(object):
    request_types = {'get': requests.get,
                     'delete': requests.delete,
                     'post': requests.post,
                     'put': requests.put}

    def __init__(self, request_type=None, resource=None):
        if request_type not in request_types:
            raise ValueError("Invalid request type: {}".format(request_type))
        self.request_type = request_type
        self.url = BASE_URL + resource

    def __call__(self, f, *args, **kwargs):
        if not Authentication.logged_in:
            raise NotLoggedInError()
        request_data = self._data_handler(f, *args, **kwargs)
        r = self.request_types[self.request_type](self._data_handler())
        if r.status_code == 200:
            return r.json()
        else:
            raise TransactionError(r)

    def _data_handler(self, *args, **kwargs):
        request_data = {}
        # f.__name__.replace converts method name to proper url
        request_data['url'] = self.url
        request_data['headers'] = Authentication.headers
        data = f(*args, **kwargs)
        if self.request_type == 'get':
            request_data['params'] = data
        else:
            request_data['data'] = json.dumps(data)
        return request_data


class User(object):
    @classmethod
    @apiCall(request_type='post',
             resource='user/allocate-now')
    def allocate_all_attributes(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/allocate')
    def allocate_attribute_point(cls, stat='str'):
        return {'stat': stat}

    @classmethod
    @apiCall(request_type='post',
             resource='user/block/:uuid')
    def block_user(cls, uuid):
        return {'uuid': uuid}

    @classmethod
    @apiCall(request_type='post',
             resource='user/buy-health-potion')
    def buy_health_potion(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/buy-mystery-set/:key')
    def buy_mystery_set(cls, key):
        return {'key': key}

    @classmethod
    @apiCall(request_type='post',
             resource='user/buy-gear/:key')
    def buy_gear(cls, key):
        return {'key': key}

    @classmethod
    @apiCall(request_type='post',
             resource='user/buy-quest/:key')
    def buy_quest(cls, key):
        return {'key': key}

    @classmethod
    @apiCall(request_type='post',
             resource='user/buy-armoire')
    def buy_armoire(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/buy/:key')
    def buy(cls, key):
        return {'key': key}

    @classmethod
    @apiCall(request_type='post',
             resource='user/buy-special-spell/:key')
    def buy_special_spell(cls, key):
        return {'key': key}

    @classmethod
    @apiCall(request_type='post',
             resource='user/class/cast/:spellId')
    def cast_spell(cls, spell_id, target_id):
        return {'spellId': spell_id,
                'targetId': target_id}

    @classmethod
    @apiCall(request_type='post',
             resource='user/change-class')
    def change_class(cls, _class):
        return {'class': _class}

    @classmethod
    @apiCall(request_type='delete',
             resource='user/messages/:id')
    def delete_message(cls, message_id=None):
        return {'id': message_id}

    @classmethod
    @apiCall(request_type='delete',
             resource='user/messages')
    def delete_all_messages(cls):
        pass

    @classmethod
    @apiCall(request_type='delete',
             resource='user')
    def delete_account(cls, password):
        return {'password': password}

    @classmethod
    @apiCall(request_type='delete',
             resource='user/auth/social/:network')
    def delete_social_authentication_method(cls, network):
        return {'network': network}

    @classmethod
    @apiCall(request_type='post',
             resource='user/disable-classes')
    def disable_classes(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/equip/:type/:key')
    def equip_item(cls, _type, key):
        return {'type': _type,
                'key': key}

    @classmethod
    @apiCall(request_type='post',
             resource='user/feed/:pet/:food')
    def feed_pet(cls, pet, food):
        return {'pet': pet,
                'food': food}

    @classmethod
    @apiCall(request_type='get',
             resource='user/anonymized')
    def get_anonymized_user_data(cls):
        pass

    @classmethod
    @apiCall(request_type='get',
             resource='user')
    def get_profile(cls):
        pass

    @classmethod
    @apiCall(request_type='get',
             resource='user/inventory/buy')
    def get_available_for_purchase(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/hatch/:egg/:hatchingPotion')
    def hatch_pet(cls, egg, hatching_potion):
        return {'egg': egg,
                'hatchingPotion': hatching_potion}

    @classmethod
    @apiCall(request_type='post',
             resource='user/sleep')
    def sleep(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/mark-pms-read')
    def mark_pms_read(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/open-mystery-item')
    def open_mystery_item(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/purchase/:type/:key')
    def purchase(cls, _type, key):
        return {'type': _type,
                'key': key}

    @classmethod
    @apiCall(request_type='post',
             resource='user/purchase-hourglass/:type/:key')
    def purchase_hourglass_item(cls, _type, key):
        return {'type': _type,
                'key': key}

    @classmethod
    @apiCall(request_type='post',
             resource='user/read-card/:cardType')
    def read_card(cls, card_type):
        return {'cardType': card_type}

    @classmethod
    @apiCall(request_type='post',
             resource='user/release-mounts')
    def release_mounts(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/release-both')
    def release_pets_and_mounts(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/reroll')
    def reroll(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/reset-password')
    def reset_password(cls, email):
        return {'email': email}

    @classmethod
    @apiCall(request_type='post',
             resource='user/reset')
    def reset(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/revive')
    def revive(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/sell/:type/:key')
    def sell(cls, _type, key):
        return {'type': _type,
                'key': key}

    @classmethod
    @apiCall(request_type='post',
             resource='user/custom-day-start')
    def custom_day_start(cls):
        pass

    @classmethod
    @apiCall(request_type='post',
             resource='user/unlock')
    def unlock(cls, path):
        return {'path': path}

    @classmethod
    @apiCall(request_type='put',
             resource='user/auth/update-email')
    def update_email(cls, new_email):
        return {'newEmail': new_email}

    @classmethod
    @apiCall(request_type='put',
             resource='user')
    def update_user(cls):
        pass

    @classmethod
    @apiCall(request_type='put',
             resource='user/auth/update-username')
    def update_username(cls, password, username):
        return {'password': password,
                'username': username}

    @classmethod
    @apiCall(request_type='post',
             resource='user/rebirth')
    def rebirth(cls):
        pass

