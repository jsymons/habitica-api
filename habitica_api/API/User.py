from .apicall import apiCall


@apiCall(request_type='put',
         resource='user/auth/update-password',
         containers=['data'])
def update_password(password, new_password, confirm_password):
    return {'password': password,
            'newPassword': new_password,
            'confirmPassword': confirm_password}


@apiCall(request_type='post',
         resource='user/allocate-now')
def allocate_all_attributes():
    pass


@apiCall(request_type='post',
         resource='user/allocate',
         containers=['params'])
def allocate_attribute_point(stat='str'):
    return {'stat': stat}


@apiCall(request_type='post',
         resource='user/block/:uuid',
         containers=['url_var'])
def block_user(uuid):
    return {'uuid': uuid}


@apiCall(request_type='post',
         resource='user/buy-health-potion')
def buy_health_potion():
    pass


@apiCall(request_type='post',
         resource='user/buy-mystery-set/:key',
         containers=['url_var'])
def buy_mystery_set(key):
    return {'key': key}


@apiCall(request_type='post',
         resource='user/buy-gear/:key',
         containers=['url_var'])
def buy_gear(key):
    return {'key': key}


@apiCall(request_type='post',
         resource='user/buy-quest/:key',
         containers=['url_var'])
def buy_quest(key):
    return {'key': key}


@apiCall(request_type='post',
         resource='user/buy-armoire')
def buy_armoire():
    pass


@apiCall(request_type='post',
         resource='user/buy/:key',
         containers=['url_var'])
def buy(key):
    return {'key': key}


@apiCall(request_type='post',
         resource='user/buy-special-spell/:key',
         containers=['url_var'])
def buy_special_spell(key):
    return {'key': key}


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


@apiCall(request_type='post',
         resource='user/change-class',
         containers=['params'])
def change_class(class_):
    return {'class': class_}


@apiCall(request_type='delete',
         resource='user/messages/:id',
         containers=['url_var'])
def delete_message(message_id=None):
    return {'id': message_id}


@apiCall(request_type='delete',
         resource='user/messages')
def delete_all_messages():
    pass


@apiCall(request_type='delete',
         resource='user',
         containers=['data'])
def delete_account(password):
    return {'password': password}


@apiCall(request_type='delete',
         resource='user/auth/social/:network',
         containers=['url_var'])
def delete_social_authentication_method(network):
    return {'network': network}


@apiCall(request_type='post',
         resource='user/disable-classes')
def disable_classes():
    pass


@apiCall(request_type='post',
         resource='user/equip/:type/:key',
         containers=['url_var'])
def equip_item(type_, key):
    return {'type': type_,
            'key': key}


@apiCall(request_type='post',
         resource='user/feed/:pet/:food',
         containers=['url_var'])
def feed_pet(pet, food):
    return {'pet': pet,
            'food': food}


@apiCall(request_type='get',
         resource='user/anonymized')
def get_anonymized_user_data():
    pass


@apiCall(request_type='get',
         resource='user')
def get_profile():
    pass


@apiCall(request_type='get',
         resource='user/inventory/buy')
def get_available_for_purchase():
    pass


@apiCall(request_type='post',
         resource='user/hatch/:egg/:hatchingPotion',
         containers=['url_var'])
def hatch_pet(egg, hatching_potion):
    return {'egg': egg,
            'hatchingPotion': hatching_potion}


@apiCall(request_type='post',
         resource='user/sleep')
def sleep():
    pass


@apiCall(request_type='post',
         resource='user/auth/local/login',
         requires_authentication=False,
         containers=['data'])
def login(username, password):
    return {'username': username, 'password': password}


@apiCall(request_type='post',
         resource='user/mark-pms-read')
def mark_pms_read():
    pass


@apiCall(request_type='post',
         resource='user/open-mystery-item')
def open_mystery_item():
    pass


@apiCall(request_type='post',
         resource='user/purchase/:type/:key',
         containers=['url_var'])
def purchase(type_, key):
    return {'type': type_,
            'key': key}


@apiCall(request_type='post',
         resource='user/purchase-hourglass/:type/:key',
         containers=['url_var'])
def purchase_hourglass_item(type_, key):
    return {'type': type_,
            'key': key}


@apiCall(request_type='post',
         resource='user/read-card/:cardType',
         containers=['url_var'])
def read_card(card_type):
    return {'cardType': card_type}


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


@apiCall(request_type='post',
         resource='user/release-mounts')
def release_mounts():
    pass


@apiCall(request_type='post',
         resource='user/release-both')
def release_pets_and_mounts():
    pass


@apiCall(request_type='post',
         resource='user/reroll')
def reroll():
    pass


@apiCall(request_type='post',
         resource='user/reset-password',
         containers=['data'])
def reset_password(email):
    return {'email': email}


@apiCall(request_type='post',
         resource='user/reset')
def reset():
    pass


@apiCall(request_type='post',
         resource='user/revive')
def revive():
    pass


@apiCall(request_type='post',
         resource='user/sell/:type/:key',
         containers=['url_var'])
def sell(type_, key):
    return {'type': type_,
            'key': key}


@apiCall(request_type='post',
         resource='user/custom-day-start')
def custom_day_start():
    pass


@apiCall(request_type='post',
         resource='user/unlock',
         containers=['params'])
def unlock(path):
    return {'path': path}


@apiCall(request_type='put',
         resource='user/auth/update-email',
         containers=['data'])
def update_email(new_email):
    return {'newEmail': new_email}


@apiCall(request_type='put',
         resource='user',
         containers=['data'])
def update_user(updates):
    return updates


@apiCall(request_type='put',
         resource='user/auth/update-username',
         containers=['data'])
def update_username(password, username):
    return {'password': password,
            'username': username}


@apiCall(request_type='post',
         resource='user/rebirth')
def rebirth():
    pass
