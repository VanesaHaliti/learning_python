import math_func


def test_add():
    assert math_func.add(7, 3) == 10 # assert means that you want to check if this code is returning a certain result
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7


def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 18
    assert math_func.product(7) == 14



