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
        cls.headers['x-api-user'] = auth['id']
        cls.headers['x-api-key'] = auth['apiToken']
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
            requires_authentication=True, containers=[]):
    request_types = {'get': requests.get,
                     'delete': requests.delete,
                     'post': requests.post,
                     'put': requests.put}
    valid_containers = ['url_var', 'params', 'data']

    def wrap(f):
        print(f.__name__)
        if request_type not in request_types:
            raise ValueError('Invalid request type: {}'.format(request_type))
        for t in containers:
            if t not in valid_containers:
                raise ValueError('Invalid data type: {}'.format(t))

        @wraps(f)
        def data_handler(*args, **kwargs):
            if requires_authentication is True and \
               Authentication.logged_in is False:
                raise NotLoggedInError()

            request_data = {}
            request_data['headers'] = Authentication.headers
            input_data = f(*args, **kwargs)
            res = resource

            def container_handler(container, c_data):
                nonlocal res
                if container == 'url_var':
                    for v in c_data:
                        if ':' in res:
                            res = res.replace(':' + v, c_data[v])
                if container == 'params':
                    request_data['params'] = c_data
                if container == 'data':
                    request_data['data'] = json.dumps(c_data)

            if len(containers) == 1:
                container_handler(containers[0], input_data)
            elif len(containers) > 1:
                for i, t in enumerate(containers):
                    container_handler(t, input_data[i])

            request_data['url'] = BASE_URL + res
            r = request_types[request_type](**request_data)
            if r.status_code in [200, 201]:
                return r.json().get('data', r.json())
            else:
                print('Status code: {}'.format(r.status_code))
                for rd in request_data:
                    print('{}:{}'.format(rd, request_data[rd]))
                raise TransactionError(r.json())

        return data_handler
    return wrap


class User(object):
    @staticmethod
    @apiCall(request_type='put',
             resource='user/auth/update-password',
             containers=['data'])
    def update_password(password, new_password, confirm_password):
        return {'password': password,
                'newPassword': new_password,
                'confirmPassword': confirm_password}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/allocate-now')
    def allocate_all_attributes():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/allocate',
             containers=['params'])
    def allocate_attribute_point(stat='str'):
        return {'stat': stat}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/block/:uuid',
             containers=['url_var'])
    def block_user(uuid):
        return {'uuid': uuid}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy-health-potion')
    def buy_health_potion():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy-mystery-set/:key',
             containers=['url_var'])
    def buy_mystery_set(key):
        return {'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy-gear/:key',
             containers=['url_var'])
    def buy_gear(key):
        return {'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy-quest/:key',
             containers=['url_var'])
    def buy_quest(key):
        return {'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy-armoire')
    def buy_armoire():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy/:key',
             containers=['url_var'])
    def buy(key):
        return {'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/buy-special-spell/:key',
             containers=['url_var'])
    def buy_special_spell(key):
        return {'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/class/cast/:spellId',
             containers=['url_var', 'params'])
    def cast_spell(spell_id, target_id=None):
        url_var = {'spellId': spell_id}
        if target_id:
            params = {'targetId': target_id}
        else:
            params = None
        return url_var, params

    @staticmethod
    @apiCall(request_type='post',
             resource='user/change-class',
             containers=['params'])
    def change_class(class_):
        return {'class': class_}

    @staticmethod
    @apiCall(request_type='delete',
             resource='user/messages/:id',
             containers=['url_var'])
    def delete_message(message_id=None):
        return {'id': message_id}

    @staticmethod
    @apiCall(request_type='delete',
             resource='user/messages')
    def delete_all_messages():
        pass

    @staticmethod
    @apiCall(request_type='delete',
             resource='user',
             containers=['data'])
    def delete_account(password):
        return {'password': password}

    @staticmethod
    @apiCall(request_type='delete',
             resource='user/auth/social/:network',
             containers=['url_var'])
    def delete_social_authentication_method(network):
        return {'network': network}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/disable-classes')
    def disable_classes():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='user/equip/:type/:key',
             containers=['url_var'])
    def equip_item(type_, key):
        return {'type': type_,
                'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/feed/:pet/:food',
             containers=['url_var'])
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
             resource='user/hatch/:egg/:hatchingPotion',
             containers=['url_var'])
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
             requires_authentication=False,
             containers=['data'])
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
             resource='user/purchase/:type/:key',
             containers=['url_var'])
    def purchase(type_, key):
        return {'type': type_,
                'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/purchase-hourglass/:type/:key',
             containers=['url_var'])
    def purchase_hourglass_item(type_, key):
        return {'type': type_,
                'key': key}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/read-card/:cardType',
             containers=['url_var'])
    def read_card(card_type):
        return {'cardType': card_type}

    @staticmethod
    @apiCall(request_type='post',
             resource='user/auth/local/register',
             requires_authentication=False,
             containers=['data'])
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
             resource='user/reset-password',
             containers=['data'])
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
             resource='user/sell/:type/:key',
             containers=['url_var'])
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
             resource='user/unlock',
             containers=['params'])
    def unlock(path):
        return {'path': path}

    @staticmethod
    @apiCall(request_type='put',
             resource='user/auth/update-email',
             containers=['data'])
    def update_email(new_email):
        return {'newEmail': new_email}

    @staticmethod
    @apiCall(request_type='put',
             resource='user',
             containers=['data'])
    def update_user(updates):
        return updates

    @staticmethod
    @apiCall(request_type='put',
             resource='user/auth/update-username',
             containers=['data'])
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
             resource='challenges',
             containers=['data'])
    def create_challenge(challenge):
        return challenge

    @staticmethod
    @apiCall(request_type='delete',
             resource='challenges/:challengeId',
             containers=['url_var'])
    def delete_challenge(challenge_id):
        return {'challengeId': challenge_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='challenges/:challengeId/export/csv',
             containers=['url_var'])
    def export_challenge_to_csv(challenge_id):
        return {'challengeId': challenge_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='challenges/:challengeId',
             containers=['url_var'])
    def get_challenge(challenge_id):
        return {'challengeId': challenge_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='challanges/groups/:groupId',
             containers=['url_var'])
    def get_challenges_for_group(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='challenges/user')
    def get_challenges_for_user():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='challenges/:challengeId/join',
             containers=['url_var'])
    def join_challenge(challenge_id):
        return {'challengeId': challenge_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='challenges/:challengeId/leave',
             containers=['url_var'])
    def leave_challenge(challenge_id):
        return {'challengeId': challenge_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='challenges/:challengeId/selectWinner/:winnerId',
             containers=['url_var'])
    def select_winner_for_challenge(challenge_id, winner_id):
        return {'challengeId': challenge_id,
                'winnerId': winner_id}

    @staticmethod
    @apiCall(request_type='put',
             resource='challenges/:challengeId',
             containers=['url_var', 'data'])
    def update_challenge(challenge_id, challenge_updates):
        url_var = {'challengeId': challenge_id}
        data = challenge_updates
        return url_var, data


class Chat(object):
    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/chat/:chatId/clearflags',
             containers=['url_var'])
    def clear_flags(group_id, chat_id):
        return {'groupId': group_id,
                'chatId': chat_id}

    @staticmethod
    @apiCall(request_type='delete',
             resource='groups/:groupId/chat/:chatId',
             containers=['url_var', 'params'])
    def delete_chat_message(previous_message, group_id, chat_id):
        url_var = {'groupId': group_id,
                   'chatId': chat_id}
        params = {'previousMsg': previous_message}
        return url_var, params

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/chat/:chatId/flag',
             containers=['url_var'])
    def flag_chat_message(group_id, chat_id):
        return {'groupId': group_id,
                'chatId': chat_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='groups/:groupId/chat',
             containers=['url_var'])
    def get_messages(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/chat/:chatId/like',
             containers=['url_var'])
    def like_message(group_id, chat_id):
        return {'groupId': group_id,
                'chatId': chat_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/chat/seen',
             containers=['url_var'])
    def mark_all_messages_from_group_read(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/chat',
             containers=['url_var', 'data', 'params'])
    def post_message(group_id, message, previous_message=None):
        url_var = {'groupId': group_id}
        data = {'message': message}
        if previous_message:
            params = {'previousMsg': previous_message}
        else:
            params = None
        return url_var, data, params


class Content(object):
    @staticmethod
    @apiCall(request_type='get',
             resource='content',
             containers=['params'])
    def get_all(language=None):
        if language:
            return {'language': language}


class Coupon(object):
    @staticmethod
    @apiCall(request_type='post',
             resource='coupons/generate/:event',
             containers=['url_var', 'params'])
    def generate(event, count_):
        url_var = {'event': event}
        params = {'count': count_}

    @staticmethod
    @apiCall(request_type='get',
             resource='coupons')
    def get():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='coupons/enter/:code',
             containers=['url_var'])
    def redeem(code):
        return {'code': code}

    @staticmethod
    @apiCall(request_type='post',
             resource='coupons/validate/:code',
             containers=['url_var'])
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
             resource='groups',
             containers=['data'])
    def create(group_data):
        return group_data

    @staticmethod
    @apiCall(request_type='get',
             resource='groups/:groupId',
             containers=['url_var'])
    def get(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='groups',
             containers=['params'])
    def get_groups_for_user(type_):
        return {'type': type_}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/invite',
             containers=['url_var', 'data'])
    def invite_to_group(group_id, email=None, emails=None,
                        name=None, uuids=None):
        if not email and not emails and not uuids:
            raise ValueError('One of email, emails, or uuids must be given')
        url_var = {'groupId': group_id}
        data = {}
        if email:
            data['email'] = email
        if emails:
            data['emails'] = emails
        if uuids:
            data['uuids'] = uuids
        return url_var, data

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/join',
             containers=['url_var'])
    def join(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/leave',
             containers=['url_var', 'params'])
    def leave(group_id, keep='keep-all'):
        url_var = {'groupId': group_id}
        params = {'keep': keep}
        return url_var, params

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/reject',
             containers=['url_var'])
    def reject_invite(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/removeMember/:memberId',
             containers=['url_var', 'params'])
    def remove_group_member(group_id, member_id, message):
        url_var = {'groupId': group_id,
                   'memberId': member_id}
        params = {'message': message}
        return url_var, params

    @staticmethod
    @apiCall(request_type='put',
             resource='groups/:groupId',
             containers=['url_var', 'data'])
    def update(group_id, group_updates):
        url_var = {'groupId': group_id}
        data = group_updates
        return url_var, data


class Hall(object):
    @staticmethod
    @apiCall(request_type='get',
             resource='hall/heroes')
    def get_heroes():
        pass

    @staticmethod
    @apiCall(request_type='get',
             resource='hall/patrons',
             containers=['params'])
    def get_patrons(page=0):
        return {'page': page}

    @staticmethod
    @apiCall(request_type='get',
             resource='hall/heroes/:heroId',
             containers=['url_var'])
    def get_hero(hero_id):
        return {'heroId': hero_id}

    @staticmethod
    @apiCall(request_type='put',
             resource='hall/heroes/:heroId',
             containers=['url_var', 'data'])
    def update_hero(hero_id, hero_updates):
        url_var = {'heroId': hero_id}
        data = hero_updates
        return url_var, data


class Member(object):
    @staticmethod
    @apiCall(request_type='get',
             resource='challenges/:challengeId/members/:memberId',
             containers=['url_var'])
    def get_challenge_member_progress(challenge_id, member_id):
        return {'challengeId': challenge_id,
                'memberId': member_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='members/:memberId',
             containers=['url_var'])
    def get_member_profile(member_id):
        return {'memberId': member_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='groups/:groupId/invites',
             containers=['url_var', 'params'])
    def get_invites_for_group(group_id, last_id=None):
        url_var = {'groupId': group_id}
        params = {}
        if last_id:
            params = {'lastId': last_id}
        return url_var, params

    @staticmethod
    @apiCall(request_type='get',
             resource='challenges/:challengeId/members',
             containers=['url_var', 'params'])
    def get_challenge_members(challenge_id, last_id=None):
        url_var = {'challengeId': challenge_id}
        params = {}
        if last_id:
            params = {'lastId': last_id}
        return url_var, params

    @staticmethod
    @apiCall(request_type='get',
             resource='groups/:groupId/members',
             containers=['url_var', 'params'])
    def get_group_members(group_id, last_id=None,
                          include_all_public_fields=None):
        url_var = {'groupId': group_id}
        params = {}
        if last_id:
            params['lastId'] = last_id
        # only available when fetching party
        if include_all_public_fields is not None:
            params['includeAllPublicFields': include_all_public_fields]
        return url_var, params

    @staticmethod
    @apiCall(request_type='post',
             resource='members/transfer-gems',
             containers=['data'])
    def transfer_gems(message, to_user, gem_amount):
        return {'message': message,
                'toUserId': to_user,
                'gemAmount': gem_amount}

    @staticmethod
    @apiCall(request_type='post',
             resource='members/send-private-message',
             containers=['data'])
    def send_private_message(message, to_user):
        return {'message': message,
                'toUserId': to_user}


class Meta(object):
    @staticmethod
    @apiCall(request_type='get',
             resource='models/:model/paths',
             requires_authentication=False,
             containers=['url_var'])
    def get_paths_for_model(model):
        return {'model': model}


class Quest(object):
    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/abort',
             containers=['url_var'])
    def abort(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/accept',
             containers=['url_var'])
    def accept(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/cancel',
             containers=['url_var'])
    def cancel_nonactive_quest(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/force-start',
             containers=['url_var'])
    def force_start(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/invite',
             containers=['url_var', 'data'])
    def invite_group(group_id, quest_key):
        url_var = {'groupId': group_id}
        data = {'questKey': quest_key}
        return url_var, data

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/leave',
             containers=['url_var'])
    def leave(group_id):
        return {'groupId': group_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='groups/:groupId/quests/reject',
             containers=['url_var'])
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
    @apiCall(request_type='post',
             resource='tags',
             containers=['data'])
    def create(tag):
        return tag

    @staticmethod
    @apiCall(request_type='delete',
             resource='tag/:tagId',
             containers=['url_var'])
    def delete(tag_id):
        return {'tagId': tag_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='tags/:tagId',
             containers=['url_var'])
    def get(tag_id):
        return {'tagId': tag_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='tags')
    def get_all():
        pass

    @staticmethod
    @apiCall(request_type='post',
             resource='reorder-tags',
             containers=['data'])
    def reorder(tag_id, to):
        return {'tagId': tag_id,
                'to': to}

    @staticmethod
    @apiCall(request_type='put',
             resource='tag/:tagId',
             containers=['url_var', 'data'])
    def update(tag_id, tag_updates):
        url_var = {'tagId': tag_id}
        data = tag_updates
        return url_var, data


class Task(object):
    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/tags/:tagId',
             containers=['url_var'])
    def add_tag(task_id, tag_id):
        return {'taskId': task_id,
                'tagId': tag_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/checklist',
             containers=['url_var', 'data'])
    def add_to_checklist(task_id, text):
        url_var = {'taskId': task_id}
        data = {'text': text}
        return url_var, data

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/approve/:userId',
             containers=['url_var'])
    def approve_user_assigned_to_group_task(task_id, user_id):
        return {'taskId': task_id,
                'userId': user_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/assign/:userId',
             containers=['url_var'])
    def assign_user_to_group_task(task_id, user_id):
        return {'taskId': task_id,
                'userId': user_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/challenge/:challengeId',
             containers=['url_var', 'data'])
    def new_challenge_task(challenge_id, tasks):
        url_var = {'challengeId': challenge}
        data = tasks
        return url_var, tasks

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/user',
             containers=['data'])
    def new(task_data):
        return task_data

    @staticmethod
    @apiCall(request_type='delete',
             resource='tasks/:taskId',
             containers=['url_var'])
    def delete(task_id):
        return {'taskId': task_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/clearCompletedTodos')
    def clear_completed_todos():
        pass

    @staticmethod
    @apiCall(request_type='get',
             resource='tasks/challenge/:challengeId',
             containers=['url_var', 'params'])
    def get_challenge_tasks(challenge_id, type_=None):
        url_var = {'challengeId': challenge_id}
        params = {}
        if type_:
            params['type'] = type_
        return url_var, params

    @staticmethod
    @apiCall(request_type='get',
             resource='tasks/:taskId',
             containers=['url_var'])
    def get(task_id):
        return {'taskId': task_id}

    @staticmethod
    @apiCall(request_type='get',
             resource='tasks/user',
             containers=['params'])
    def get_all(type_=None):
        if type_:
            return {'type': type_}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/move/to/:position',
             containers=['url_var'])
    def move(task_id, position):
        return {'taskId': task_id,
                'position': position}

    @staticmethod
    @apiCall(request_type='delete',
             resource='tasks/:taskId/checklist/:itemId',
             containers=['url_var'])
    def delete_from_checklist(task_id, item_id):
        return {'taskId': task_id,
                'itemId': item_id}

    @staticmethod
    @apiCall(request_type='delete',
             resource='tasks/:taskId/tags/:tagId',
             containers=['url_var'])
    def remove_tag(task_id, tag_id):
        return {'taskId': task_id,
                'tagId': tag_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/checklist/:itemId/score',
             containers=['url_var'])
    def score_checklist_item(task_id, item_id):
        return {'taskId': task_id,
                'itemId': item_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/score/:direction',
             containers=['url_var'])
    def score(task_id, direction='up'):
        return {'taskId': task_id,
                'direction': direction}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/:taskId/unassign/:userId',
             containers=['url_var'])
    def unassign_user_from_group_task(task_id, user_id):
        return {'taskId': task_id,
                'userId': user_id}

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/unlink-one/:taskId',
             containers=['url_var', 'params'])
    def unlink_from_challenge(task_id, keep):
        url_var = {'taskId': task_id}
        params = {'keep': keep}
        return url_var, params

    @staticmethod
    @apiCall(request_type='post',
             resource='tasks/unlink-all/:challengeId',
             containers=['url_var', 'params'])
    def unlink_all_from_challenge(challenge_id, keep):
        url_var = {'challengeId': challenge_id}
        params = {'keep': keep}
        return url_var, params

    @staticmethod
    @apiCall(request_type='put',
             resource='tasks/:taskId/checklist/:itemId',
             containers=['url_var', 'data'])
    def update_checklist_item(task_id, item_id, text):
        url_var = {'taskId': task_id,
                   'itemId': item_id}
        data = {'text': text}
        return url_var, data

    @staticmethod
    @apiCall(request_type='put',
             resource='tasks/:taskId',
             containers=['url_var', 'data'])
    def update(task_id, task_updates):
        url_var = {'taskId': task_id}
        data = task_updates
        return url_var, data
