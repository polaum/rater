from pymongo import MongoClient


class ConsumptionException(Exception):
    pass


client = MongoClient()

users_db = client['users_db']
users = users_db['users_collection']


class User:
    def __init__(self, userid: int, limit=None):
        user = users.find_one({'user_id': userid})
        if user:
            # user exists
            self.consumption = user['consumption']
            self.limit = user['limit']
        else:
            # new user
            users.insert_one({'user_id': userid,'consumption': 0, 'limit': limit})
            self.consumption = 0
            self.limit = limit
        self._userid = userid

    @property
    def userid(self):
        return self._userid

    def _can_consume(self, desired_added_cons=0):
        if not self.limit:
            return True
        return self.limit >= (self.consumption + desired_added_cons)

    def consume(self, added_cons: int):
        if self._can_consume(added_cons):
            self.consumption += added_cons
            this_user = users.find_one({'user_id': self.userid})
            this_user['consumption'] = self.consumption
            users.save(this_user)
        else:
            raise ConsumptionException('User not allowed to consume this')
