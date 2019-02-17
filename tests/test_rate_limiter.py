import pytest
import random

from rater_func import User, ConsumptionException

def test_creating_user_same_id():
    num = random.randint(0,10000)
    polala = User(num, 5)
    assert User(num).limit == 5
    assert User(num, 10).limit == 5


def test_can_consume():
    pola = User(random.randint(0,10000), 4)
    samer = User(random.randint(0,10000))
    assert pola._can_consume(10) == False
    assert pola._can_consume(2) == True
    assert samer._can_consume(random.randint(0,100)) == True
    pola.consume(3)
    assert pola._can_consume(2) == False


def test_update_consumption():
    matan = User(random.randint(0,10000), 10)
    matan.consume(5)
    assert matan.cons == 5
    with pytest.raises(ConsumptionException):
        matan.consume(10)

