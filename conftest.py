import pytest
from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle


@pytest.fixture(scope='module')
def create_circle():
    return Circle(10)


@pytest.fixture(scope='module')
def create_correct_triangle():
    return Triangle(3, 4, 5)


@pytest.fixture(scope='module')
def create_incorrect_triangle():
    return Triangle(1, 2, 3)


@pytest.fixture(scope='module')
def create_rectangle():
    return Rectangle(2, 5)


@pytest.fixture(scope='module')
def create_square():
    return Square(10)


