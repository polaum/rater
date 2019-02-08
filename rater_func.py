class ConsumptionException(Exception):
    pass


class UserCreationException(Exception):
    pass


users = []


class User:
    def __init__(self, userid, limit=None):
        self.userid = userid
        self.limit = limit
        self.consumption = 0
        if self.userid not in users:
            users.append(userid)
        else:
            raise UserCreationException("This user ID is already exist")

    def check_consumption(self):
        return self.consumption

    def set_limit(self, new_limit):
        self.limit = new_limit

    def check_limit(self):
        return self.limit

    def can_consume(self, desired_added_cons=0):
        if self.check_limit() == None:
            return True
        return self.check_limit() >= (self.check_consumption() + desired_added_cons)

    def update_consumption(self, added_cons):
        if self.can_consume(added_cons):
            self.consumption += added_cons
        else:
            raise ConsumptionException('User not allowed to consume this')