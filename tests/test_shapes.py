import pytest

from src.Figure import Figure
from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle


def test_check_triangle_exists():
    triangle = Triangle(3, 4, 5)
    assert triangle.check_triangle_to_exist()


def test_check_triangle_doesnt_exists():
    triangle = Triangle(1, 2, 3)
    assert triangle.check_triangle_to_exist() is None


def test_check_triangle_has_name():
    triangle = Triangle(1, 2, 3)
    assert hasattr(triangle, 'name')


def test_check_triangle_has_perimeter():
    triangle = Triangle(1, 2, 3)
    assert hasattr(triangle, 'perimeter')


def test_check_triangle_has_area():
    triangle = Triangle(1, 2, 3)
    assert hasattr(triangle, 'area')


def test_check_triangle_add_area():
    triangle = Triangle(3, 4, 5)
    square = Square(10)
    assert triangle.add_area(square) == 106


def test_check_rectangle_has_name():
    rectangle = Rectangle(1, 2)
    assert hasattr(rectangle, 'name')


def test_check_rectangle_has_perimeter():
    rectangle = Rectangle(1, 2)
    assert hasattr(rectangle, 'perimeter')


def test_check_rectangle_has_area():
    rectangle = Rectangle(1, 2)
    assert hasattr(rectangle, 'area')


def test_check_rectangle_add_area():
    rectangle = Rectangle(1, 2)
    triangle = Triangle(3, 4, 5)
    assert rectangle.add_area(triangle) == 8


def test_check_square_has_name():
    square = Square(10)
    assert hasattr(square, 'name')


def test_check_square_has_perimeter():
    square = Square(10)
    assert hasattr(square, 'perimeter')


def test_check_square_has_area():
    square = Square(10)
    assert hasattr(square, 'area')


def test_check_square_add_area():
    square = Square(10)
    circle = Circle(10)
    assert round(square.add_area(circle), 2) == 414.16


def test_check_circle_has_name():
    circle = Circle(1)
    assert hasattr(circle, 'name')


def test_check_circle_has_perimeter():
    circle = Circle(1)
    assert hasattr(circle, 'perimeter')


def test_check_circle_has_area():
    circle = Circle(1)
    assert hasattr(circle, 'area')


def test_check_circle_add_area():
    circle = Circle(1)
    rectangle = Rectangle(5, 2)
    assert round(circle.add_area(rectangle), 2) == 13.14


def test_check_add_area_value_error():
    circle = Circle(1)
    with pytest.raises(ValueError):
        circle.add_area('lalala')
