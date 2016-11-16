import requests
import json
from functools import wraps

BASE_URL = "https://habitica.com/api/v3/"


class Authentication(object):
    headers = {'content-type': 'application/json'}
    logged_in = False

    @classmethod
    def login(cls, username, password):
        auth = User.login(username, password)
        print('logged in')
        cls.headers['x-api-user'] = auth['data']['id']
        cls.headers['x-api-key'] = auth['data']['apiToken']
        cls.logged_in = True

    @classmethod
    def logout(cls):
        if logged_in:
            cls.headers.pop('x-api-user')
            cls.headers.pop('x-api-key')
            cls.logged_in = False


class NotLoggedInError(Exception):
    pass


class TransactionError(Exception):
    pass


def apiCall(request_type=None, resource=None,
            requires_authentication=True):
    request_types = {'get': requests.get,
                     'delete': requests.delete,
                     'post': requests.post,
                     'put': requests.put}

    def wrap(f):
        print(f.__name__)
        if request_type not in request_types:
            raise ValueError('Invalid request type: {}'.format(request_type))

        @wraps(f)
        def data_handler(*args, **kwargs):
            if requires_authentication is True and \
               Authentication.logged_in is False:
                raise NotLoggedInError()

            request_data = {}
            request_data['headers'] = Authentication.headers
            data = f(*args, **kwargs)
            res = resource
            for d in data:
                if ':' + d in res:
                    res = res.replace(':' + d, data[d])
            request_data['url'] = BASE_URL + res
            if request_type == 'get':
                request_data['params'] = data
            else:
                request_data['data'] = json.dumps(data)

            r = request_types[request_type](**request_data)
            if r.status_code == 200:
                return r.json()
            else:
                raise TransactionError(r)

        return data_handler
    return wrap

'''
class apiCall(object):
    request_types = {'get': requests.get,
                     'delete': requests.delete,
                     'post': requests.post,
                     'put': requests.put}

    def __init__(self, request_type=None, resource=None,
                 requires_authentication=True):
        if request_type not in self.request_types:
            raise ValueError("Invalid request type: {}".format(request_type))
        self.request_type = request_type
        self.requires_authentication = requires_authentication
        self.resource = resource
        functools.update_wrapper(self, func)

    def __call__(self, f, *args, **kwargs):
        if self.requires_authentication and not Authentication.logged_in:
            raise NotLoggedInError()
        request_data = self._data_handler(f, *args, **kwargs)
        r = self.request_types[self.request_type](self._data_handler())
        if r.status_code == 200:
            return r.json()
        else:
            raise TransactionError(r)

    def _data_handler(self,f, *args, **kwargs):
        request_data = {}
        request_data['headers'] = Authentication.headers
        data = f(*args, **kwargs)
        res = self.resource
        for d in data:
            if ':' + d in res:
                res = res.replace(':' + d, data[d])
        request_data['url'] = BASE_URL + res
        if self.request_type == 'get':
            request_data['params'] = data
        else:
            request_data['data'] = json.dumps(data)
        return request_data
'''


class User(object):
    @staticmethod
    @apiCall(request_type='post',
             resource='user/allocate-now')
    def allocate_all_attributes():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/allocate')
    def allocate_attribute_point(stat='str'):
        return {'stat': stat}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/block/:uuid')
    def block_user(uuid):
        return {'uuid': uuid}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy-health-potion')
    def buy_health_potion():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy-mystery-set/:key')
    def buy_mystery_set(key):
        return {'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy-gear/:key')
    def buy_gear(key):
        return {'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy-quest/:key')
    def buy_quest(key):
        return {'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy-armoire')
    def buy_armoire():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy/:key')
    def buy(key):
        return {'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy-special-spell/:key')
    def buy_special_spell(key):
        return {'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/class/cast/:spellId')
    def cast_spell(spell_id, target_id):
        return {'spellId': spell_id,
                'targetId': target_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/change-class')
    def change_class(class_):
        return {'class': class_}

    @staticmethod
    @apiCall(request_type='delete',
             resource='user/messages/:id')
    def delete_message(message_id=None):
        return {'id': message_id}

    @staticmethod
    @apiCall(request_type='delete',
             resource='user/messages')
    def delete_all_messages():
        pass

    @staticmethod
    @apiCall(request_type='delete',
             resource='user')
    def delete_account(password):
        return {'password': password}

    @staticmethod
    @apiCall(request_type='delete',
             resource='user/auth/social/:network')
    def delete_social_authentication_method(network):
        return {'network': network}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/disable-classes')
    def disable_classes():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/equip/:type/:key')
    def equip_item(type_, key):
        return {'type': type_,
                'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/feed/:pet/:food')
    def feed_pet(pet, food):
        return {'pet': pet,
                'food': food}

    @staticmethod
    @apiCall(request_type='get',
             resource='user/anonymized')
    def get_anonymized_user_data():
        pass

    @staticmethod
    @apiCall(request_type='get',
             resource='user')
    def get_profile():
        pass

    @staticmethod
    @apiCall(request_type='get',
             resource='user/inventory/buy')
    def get_available_for_purchase():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/hatch/:egg/:hatchingPotion')
    def hatch_pet(egg, hatching_potion):
        return {'egg': egg,
                'hatchingPotion': hatching_potion}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/sleep')
    def sleep():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/auth/local/login',
             requires_authentication=False)
    def login(username, password):
        return {'username': username, 'password': password}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/mark-pms-read')
    def mark_pms_read():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/open-mystery-item')
    def open_mystery_item():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/purchase/:type/:key')
    def purchase(type_, key):
        return {'type': type_,
                'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/purchase-hourglass/:type/:key')
    def purchase_hourglass_item(type_, key):
        return {'type': type_,
                'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/read-card/:cardType')
    def read_card(card_type):
        return {'cardType': card_type}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/auth/local/register',
             requires_authentication=False)
    def register_new_user(username, email, password, confirm_password):
        return {'username': username,
                'email': email,
                'password': password,
                'confirmPassword': confirm_password
                }

    @staticmethod
    @apiCall(request_type='post',
             resource='user/release-mounts')
    def release_mounts():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/release-both')
    def release_pets_and_mounts():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/reroll')
    def reroll():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/reset-password')
    def reset_password(email):
        return {'email': email}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/reset')
    def reset():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/revive')
    def revive():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/sell/:type/:key')
    def sell(type_, key):
        return {'type': type_,
                'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/custom-day-start')
    def custom_day_start():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/unlock')
    def unlock(path):
        return {'path': path}

    @staticmethod
    @apiCall(request_type='put',
             resource='user/auth/update-email')
    def update_email(new_email):
        return {'newEmail': new_email}

    @staticmethod
    @apiCall(request_type='put',
             resource='user')
    def update_user():
        pass

    @staticmethod
    @apiCall(request_type='put',
             resource='user/auth/update-username')
    def update_username(password, username):
        return {'password': password,
                'username': username}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/rebirth')
    def rebirth():
        pass


class Challenge(object):
    @staticmethod
    @apiCall(request_type='post',
             resource='challenges')
    def create_challenge():
        pass

    @staticmethod
    @apiCall(request_type='delete',
             resource='challenges/:challengeId')
    def delete_challenge(challenge_id):
        return {'challengeId': challenge_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='challenges/:challengeId/export/csv')
    def export_challenge_to_csv(challenge_id):
        return {'challengeId': challenge_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='challenges/:challengeId')
    def get_challenge(challenge_id):
        return {'challengeId': challenge_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='challanges/groups/:groupId')
    def get_challenges_for_group(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='challenges/user')
    def get_challenges_for_user():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='challenges/:challengeId/join')
    def join_challenge(challenge_id):
        return {'challengeId': challenge_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='challenges/:challengeId/leave')
    def leave_challenge(challenge_id):
        return {'challengeId': challenge_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='challenges/:challengeId/selectWinner/:winnerId')
    def select_winner_for_challenge(challenge_id, winner_id):
        return {'challengeId': challenge_id,
                'winnerId': winner_id}

    @staticmethod
    @apiCall(request_type='put',
             resource='challenges/:challengeId')
    def update_challenge(challenge_id):
        return {'challengeId': challenge_id}


class Chat(object):
    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/chat/:chatId/clearflags')
    def clear_flags(group_id, chat_id):
        return {'groupId': group_id,
                'chatId': chat_id}

    @staticmethod
    @apiCall(request_type='delete',
             resource='groups/:groupId/chat/:chatId')
    def delete_chat_message(previous_message, group_id, chat_id):
        return {'previousMsg': previous_message,
                'groupId': group_id,
                'chatId': chat_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/chat/:chatId/flag')
    def flag_chat_message(group_id, chat_id):
        return {'groupId': group_id,
                'chatId': chat_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='groups/:groupId/chat')
    def get_messages(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/chat/:chatId/like')
    def like_message(group_id, chat_id):
        return {'groupId': group_id,
                'chatId': chat_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/chat/seen')
    def mark_all_messages_from_group_read(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/chat')
    def post_message(group_id):
        return {'groupId': group_id}


class Content(object):
    @staticmethod
    @apiCall(request_type='get',
             resource='content')
    def get_all(language=None):
        if language:
            return {'language': language}


class Coupon(object):
    @staticmethod
    @apiCall(request_type='post',
             resource='coupons/generate/:event')
    def generate(event, count_):
        return {'event': event,
                'count': count_}

    @staticmethod
    @apiCall(request_type='get',
             resource='coupons')
    def get():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='coupons/enter/:code')
    def redeem(code):
        return {'code': code}

    @staticmethod
    @apiCall(request_type='post',
             resource='coupons/validate/:code')
    def validate(code):
        return {'code': code}


class Development(object):
    @staticmethod
    @apiCall(request_type='post',
             resource='debug/add-hourglass')
    def add_hourglass_to_user():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='debug/add-ten-gems')
    def add_ten_gems_to_user():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='debug/quest-progress')
    def accelerate_quest_progress():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='debug/modify-inventory')
    def modify_user_inventory():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='debug/make-admin')
    def make_admin():
        pass


class Group(object):
    @staticmethod
    @apiCall(request_type='post',
             resource='groups')
    def create():
        pass

    @staticmethod
    @apiCall(request_type='get',
             resource='groups/:groupId')
    def get(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='groups')
    def get_groups_for_user(type_):
        return {'type': type_}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/invite')
    def invite_to_group(group_id, email=None, emails=None,
                        name=None, uuids=None):
        if not email and not emails and not uuids:
            raise ValueError('One of email, emails, or uuids must be given')
        data = {'groupId': group_id}
        if email:
            data['email'] = email
        if emails:
            data['emails'] = emails
        if uuids:
            data['uuids'] = uuids
        return data

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/join')
    def join(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/leave')
    def leave(group_id, keep=None):
        data = {'groupId': group_id}
        if keep:
            data['keep'] = keep
        return data

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/reject')
    def reject_invite(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/removeMember/:memberId')
    def remove_group_member(group_id, member_id, message):
        return {'groupId': group_id,
                'memberId': member_id,
                'message': message}

    @staticmethod
    @apiCall(request_type='put',
             resource='groups/:groupId')
    def update(group_id):
        return {'groupId': group_id}


class Hall(object):
    @staticmethod
    @apiCall(request_type='get',
             resource='hall/heroes')
    def get_heroes():
        pass

    @staticmethod
    @apiCall(request_type='get',
             resource='hall/patrons')
    def get_patrons(page=None):
        if page:
            return {'page': page}

    @staticmethod
    @apiCall(request_type='get',
             resource='hall/heroes/:heroId')
    def get_hero(hero_id):
        return {'heroId': hero_id}

    @staticmethod
    @apiCall(request_type='put',
             resource='hall/heroes/:heroId')
    def update_hero(hero_id):
        return {'heroId': hero_id}


class Member(object):
    @staticmethod
    @apiCall(request_type='get',
             resource='challenges/:challengeId/members/:memberId')
    def get_challenge_member_progress(challenge_id, member_id):
        return {'challengeId': challenge_id,
                'memberId': member_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='members/:memberId')
    def get_member_profile(member_id):
        return {'memberId': member_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='groups/:groupId/invites')
    def get_invites_for_group(group_id, last_id=None):
        data = {'groupId': group_id}
        if last_id:
            data['lastId'] = last_id
        return data

    @staticmethod
    @apiCall(request_type='get',
             resource='challenges/:challengeId/members')
    def get_challenge_members(challenge_id, last_id=None):
        data = {'challengeId': challenge_id}
        if last_id:
            data['lastId'] = last_id
        return data

    @staticmethod
    @apiCall(request_type='get',
             resource='groups/:groupId/members')
    def get_group_members(group_id, last_id=None,
                          include_all_public_fields=False):
        data = {'groupId': group_id}
        if last_id:
            data['lastId'] = last_id
        # only available when fetching party
        if include_all_public_fields is True:
            data['includeAllPublicFields': True]
        return data

    @staticmethod
    @apiCall(request_type='post',
             resource='members/transfer-gems')
    def transfer_gems(message, to_user, gem_amount):
        return {'message': message,
                'toUserId': to_user,
                'gemAmount': gem_amount}

    @staticmethod
    @apiCall(request_type='post',
             resource='members/send-private-message')
    def send_private_message(message, to_user):
        return {'message': message,
                'toUserId': to_user}


class Meta(object):
    @staticmethod
    @apiCall(request_type='get',
             resource='models/:model/paths',
             requires_authentication=False)
    def get_paths_for_model(model):
        return {'model': model}


class Quest(object):
    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/abort')
    def abort(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/accept')
    def accept(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/cancel')
    def cancel_nonactive_quest(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/force-start')
    def force_start(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/invite')
    def invite_group(group_id, quest_key):
        return {'groupId': group_id,
                'questKey': quest_key}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/leave')
    def leave(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/reject')
    def reject(group_id):
        return {'groupId': group_id}


class Status(object):
    @staticmethod
    @apiCall(request_type='get',
             resource='status',
             requires_authentication=False)
    def get():
        pass


class Tag(object):
    @staticmethod
    @apiCall(request_type='delete',
             resource='tag/:tagId')
    def delete(tag_id):
        return {'tagId': tag_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='tags/:tagId')
    def get(tag_id):
        return {'tagId': tag_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='tags')
    def get_all():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='reorder-tags')
    def reorder(tag_id, to):
        return {'tagId': tag_id,
                'to': to}

    @staticmethod
    @apiCall(request_type='put',
             resource='tag/:tagId')
    def update(tag_id):
        return {'tagId': tag_id}


class Task(object):
    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/checklist')
    def add_to_checklist(task_id):
        return {'taskId': task_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/approve/:userId')
    def approve_user_assigned_to_group_task(task_id, user_id):
        return {'taskId': task_id,
                'userId': user_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/assign/:userId')
    def assign_user_to_group_task(task_id, user_id):
        return {'taskId': task_id,
                'userId': user_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/challenge/:challengeId')
    def new_challenge_task(challenge_id):
        return {'challengeId': challenge}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/user')
    def new():
        pass

    @staticmethod
    @apiCall(request_type='delete',
             resource='tasks/:taskId')
    def delete(task_id):
        return {'taskId': task_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/clearCompletedTodos')
    def clear_completed_todos():
        pass

    @staticmethod
    @apiCall(request_type='get',
             resource='tasks/challenge/:challengeId')
    def get_challenge_tasks(challenge_id, type_=None):
        data = {'challengeId': challenge_id}
        if type_:
            data['type'] = type_
        return data

    @staticmethod
    @apiCall(request_type='get',
             resource='tasks/:taskId')
    def get(task_id):
        return {'taskId': task_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='tasks/user')
    def get_all(type_=None):
        if type_:
            return {'type': type_}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/move/to/:position')
    def move(task_id, position):
        return {'taskId': task_id,
                'position': position}

    @staticmethod
    @apiCall(request_type='delete',
             resource='tasks/:taskId/checklist/:itemId')
    def delete_from_checklist(task_id, item_id):
        return {'taskId': task_id,
                'itemId': item_id}

    @staticmethod
    @apiCall(request_type='delete',
             resource='tasks/:taskId/tags/:tagId')
    def remove_tag(task_id, tag_id):
        return {'taskId': task_id,
                'tagId': tag_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/checklist/:itemId/score')
    def score_checklist_item(task_id, item_id):
        return {'taskId': task_id,
                'itemId': item_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/score/:direction')
    def score(task_id, direction='up'):
        return {'taskId': task_id,
                'direction': direction}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/unassign/:userId')
    def unassign_user_from_group_task(task_id, user_id):
        return {'taskId': task_id,
                'userId': user_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/unlink-one/:taskId')
    def unlink_from_challenge(task_id, keep):
        return {'taskId': task_id,
                'keep': keep}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/unlink-all/:challengeId')
    def unlink_all_from_challenge(challenge_id, keep):
        return {'challengeId': challenge_id,
                'keep': keep}

    @staticmethod
    @apiCall(request_type='put',
             resource='tasks/:taskId/checklist/:itemId')
    def update_checklist_item(task_id, item_id):
        return {'taskId': task_id,
                'itemId': item_id}

    @staticmethod
    @apiCall(request_type='put',
             resource='tasks/:taskId')
    def update(task_id):
        return {'taskId': task_id}
