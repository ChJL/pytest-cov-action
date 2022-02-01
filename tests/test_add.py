from src.add import add_fun
from src.multi import multi_fun


def test_add_fun():
    assert add_fun(1, 4) == 5
    assert add_fun(2, 4) == 6
    assert add_fun(3, 4) == 7
    assert add_fun(6, 4) == 10


def test_add_fun2():
    assert add_fun(5, 5) == 10
    assert add_fun(2, 4) == 2
    assert add_fun(3, 4) == 4
    assert add_fun(6, 12) == 18


def test_multi_fun():
    assert multi_fun(1, 4) == 4
    assert multi_fun(2, 4) == 8
    assert multi_fun(3, 4) == 12
    assert multi_fun(6, 4) == 24