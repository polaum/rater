import pytest
import random

from rater_func import User, ConsumptionException

def test_creating_user_same_id():
    polala = User(2, 5)
    assert User(2).limit == 5
    assert User(2, 10).limit == 5


def test_can_consume():
    pola = User(1, 4)
    samer = User(3)
    assert pola._can_consume(10) == False
    assert pola._can_consume(2) == True
    assert samer._can_consume(random.randrange(100)) == True
    pola.consume(3)
    assert pola._can_consume(2) == False


def test_update_consumption():
    matan = User(4, 10)
    matan.consume(5)
    assert matan.consumption == 5
    with pytest.raises(ConsumptionException):
        matan.consume(10)

