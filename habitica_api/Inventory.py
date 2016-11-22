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
    def __init__(self):
        self.items = []
        data = self._get_data()
        for item in data:
            self.items.append(Item(**item))

    def _get_data(self):
        return API.User.get_profile()['items'][self.item_type]

    def __iter__(self):
        for i in self.items:
            yield i

    def __len__(self):
        return len(self.items)


class Purchasables(QuerySet):
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


class EquipmentQuerySet(QuerySet):
    def __init__(self):
        self.items = []
        data = self._get_data()
        for item in data.values():
            self.items.append(Item(key=item))


class Equipped(EquipmentQuerySet):
    def _get_data(self):
        return API.User.get_profile()['items']['gear']['equipped']


class Costume(EquipmentQuerySet):
    def _get_data(self):
        return API.User.get_profile()['items']['gear']['costume']


class Gear(QuerySet):
    def __init__(self):
        self.items = []
        data = self._get_data()
        for item in data.keys():
            if data[item] is True:
                self.items.append(Item(key=item))

    def _get_data(self):
        return API.User.get_profile()['items']['gear']['owned']