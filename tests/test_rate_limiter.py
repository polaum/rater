import pytest
import random

from rater_func import User, ConsumptionException, UserCreationException

def test_creating_user_same_id():
    polala = User(2)
    with pytest.raises(UserCreationException):
        another_pola = User(2)


def test_can_consume():
    pola = User(1, 4)
    samer = User(3)
    assert pola.can_consume(10) == False
    assert pola.can_consume(2) == True
    assert samer.can_consume(random.randrange(100)) == True
    pola.update_consumption(3)
    assert pola.can_consume(2) == False


def test_update_consumption():
    matan = User(4, 10)
    matan.update_consumption(5)
    assert matan.check_consumption() == 5
    with pytest.raises(ConsumptionException):
        matan.update_consumption(10)

