from pymongo import MongoClient


class ConsumptionException(Exception):
    pass


client = MongoClient()

users_db = client['users_db']
users = users_db['users_collection']


class User:
    def __init__(self, userid: int, limit=None):
        self.db_user_doc = users.find_one({'user_id': userid})
        if not self.db_user_doc:
            # new user
            users.insert_one({'user_id': userid,'consumption': 0, 'limit': limit})
            self.db_user_doc = users.find_one({'user_id': userid})

    @property
    def userid(self):
        return self.db_user_doc['user_id']

    @property
    def cons(self) -> int:
        return int(self.db_user_doc['consumption'])

    @property
    def limit(self) -> int:
        _value = self.db_user_doc['limit']
        if _value:
            return int(_value)

    @cons.setter
    def cons(self, value: int):
        self.db_user_doc['consumption'] = self.cons + value
        users.save(self.db_user_doc)

    @limit.setter
    def limit(self, value: int):
        self.db_user_doc['limit'] = value
        users.save(self.db_user_doc)

    def _can_consume(self, desired_added_cons=0):
        if not self.limit:
            return True
        return self.limit >= (self.cons + desired_added_cons)

    def consume(self, added_cons: int):
        if self._can_consume(added_cons):
            self.cons += added_cons
        else:
            raise ConsumptionException('User not allowed to consume this')
