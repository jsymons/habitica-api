from . import API


class User():

    active = None
    purchasable_list = []
    inventory = {}

    @classmethod
    def update_status(self):
        status = API.User.get_profile()
        if status is not None:
            #extract stats block first
            for stat in status['stats']:
                setattr(self, stat, status['stats'][stat])
            status.pop('stats')
            for key in status:
                setattr(self, key, status[key])
            return True
        else:
            return False

    @classmethod
    def _update_stats(self, data):
        for stat in data:
            setattr(self, stat, data[stat])
