import pytest


def func(a, b):
    return a * b


def testfunc():
    assert func(2, 2) == 4
    assert func(3, 3) == 9


if __name__ == '__main__':
    pytest.main()

