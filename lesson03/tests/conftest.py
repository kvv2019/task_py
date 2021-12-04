import math
import random

import pytest

from lesson03.src.Circle import Circle
from lesson03.src.Rectangle import Rectangle
from lesson03.src.Square import Square
from lesson03.src.Triangle import Triangle


def rnd_value():
    return (lambda x: 0.1 if x == 0 else x)(random.random())


def calc_param3(param1, param2):
    return math.sqrt(param1 ** 2 + param2 ** 2 - 2 * param1 * param2 * math.cos(random.randint(1, 179)))


@pytest.fixture
def figure_reg(test_figure, test_param1, test_param2, test_param3):
    if issubclass(test_figure, Circle) or issubclass(test_figure, Square):
        return test_figure(test_param1)
    elif issubclass(test_figure, Rectangle):
        return test_figure(test_param1, test_param2)
    elif issubclass(test_figure, Triangle):
        return test_figure(test_param1, test_param2, test_param3)
    else:
        raise ValueError('Передан неожиданный класс')


@pytest.fixture
def figure_rnd(test_figure):
    if issubclass(test_figure, Circle) or issubclass(test_figure, Square):
        return test_figure(rnd_value())
    elif issubclass(test_figure, Rectangle):
        return test_figure(rnd_value(), rnd_value())
    elif issubclass(test_figure, Triangle):
        param1 = rnd_value()
        param2 = rnd_value()
        param3 = calc_param3(param1, param2)
        return test_figure(param1, param2, param3)
    else:
        raise ValueError('Передан неожиданный класс')


@pytest.fixture
def circle_rnd():
    return Circle(rnd_value())


@pytest.fixture
def square_rnd():
    return Square(rnd_value())


@pytest.fixture
def rectangle_rnd():
    return Rectangle(rnd_value(), rnd_value())


@pytest.fixture
def triangle_rnd():
    param1 = rnd_value()
    param2 = rnd_value()
    param3 = calc_param3(param1, param2)
    return Triangle(param1, param2, param3)
