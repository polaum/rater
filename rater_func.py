class ConsumptionException(Exception):
    pass


users = {}


class User:
    def __init__(self, userid: int, limit=None):
        if userid in users:
            # user exists
            self.consumption = users[userid]['consumption']
            self.limit = users[userid]['limit']
        else:
            # new user
            users[userid] = {'consumption': 0, 'limit': limit}
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
            users[self.userid]['consumption'] = self.consumption
        else:
            raise ConsumptionException('User not allowed to consume this')
