from . import API
from .user import User


class Item(object):
    def __init__(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])

    def buy(self):
        API.User.buy(self.key)


def buy_health_potion():
    updated_stats = API.User.buy_health_potion()
    User._update_stats(updated_stats)


class QuerySet(object):
    @classmethod
    def update(self, data=None):
        if data is None:
            self._get_data()
        for item in data:
            self.items.append(Item(**item))

    @classmethod
    def _get_data(self):
        return API.User.get_profile()['items'][self.item_type]

    @classmethod
    def __iter__(self):
        for i in self.items:
            yield i


class Purchasables(QuerySet):
    @classmethod
    def _get_data(self):
        return API.User.get_available_for_purchase()


class Mounts(QuerySet):
    item_type = 'mounts'


class Quests(QuerySet):
    item_type = 'quests'


class Food(QuerySet):
    item_type = 'food'


class HatchingPotions(QuerySet):
    item_type = 'hatchingPotions'


class Eggs(QuerySet):
    item_type = 'eggs'


class Pets(QuerySet):
    item_type = 'pets'


class Equipped(QuerySet):
    @classmethod
    def _get_data(self):
        return API.User.get_profile()['items']['gear']['equipped']


class Costume(QuerySet):
    @classmethod
    def _get_data(self):
        return API.User.get_profile()['items']['gear']['costume']


class Gear(QuerySet):
    @classmethod
    def _get_data(self):
        return API.User.get_profile()['items']['gear']['owned']