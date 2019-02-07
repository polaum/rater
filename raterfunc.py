import pytest
class ConsumptionException(Exception):
    print("User not allowed to consume this")


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
            raise ConsumptionException

pola = User(1, 4)

def test_can_consume():
    assert pola.can_consume(10) == False
    assert pola.can_consume(2) == True
    pola.update_consumption(3)
    assert pola.can_consume(2) == False

matan = User(2, 10)

def test_update_consumption():
    matan.update_consumption(5)
    assert matan.check_consumption() == 5
    with pytest.raises(ConsumptionException):
        matan.update_consumption(10)





