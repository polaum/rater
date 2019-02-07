import pytest

class User:
    def __init__(self, userid, limit = None):
        self.userid = userid
        self.limit = limit
        self.consumption = 0

    def check_consumption(self):
        return self.consumption

    def set_limit(self, new_limit):
        self.limit = new_limit

    def check_limit(self):
        return self.limit

    def can_consume(self, desired_added_cons = 0):
        return self.check_limit() >= (self.check_consumption() + desired_added_cons)

    def update_consumption(self, added_cons):
        if self.can_consume(added_cons):
            self.consumption += added_cons
        else:
            print("User not allowed to consume this")

pola = User(1, 4)

def test_can_consume(user: User):
    assert pola.can_consume(10) == True
    assert pola.can_consume(range(pola.limit)) == True

print(pola.check_consumption())
pola.update_consumption(5)
print(pola.check_consumption())
pola.update_consumption(3)
print(pola.check_consumption())


