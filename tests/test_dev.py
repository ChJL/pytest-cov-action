from src.dev import dev_fun


def test_add_fun():
    assert dev_fun(4, 4) == 1
    assert dev_fun(8, 4) == 2
    assert dev_fun(6, 2) == 3
    assert dev_fun(10, 5) == 2