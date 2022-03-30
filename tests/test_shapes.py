import pytest
# from src.Triangle import Triangle
# from src.Square import Square
# from src.Circle import Circle
# from src.Rectangle import Rectangle


def test_check_triangle_exists(create_correct_triangle):
    assert create_correct_triangle.existance


def test_check_triangle_doesnt_exists(create_incorrect_triangle):
    assert create_incorrect_triangle.existance is None


def test_check_triangle_has_name(create_correct_triangle):
    assert hasattr(create_correct_triangle, 'name')


def test_check_triangle_has_perimeter(create_correct_triangle):
    assert hasattr(create_correct_triangle, 'perimeter')


def test_check_triangle_has_area(create_correct_triangle):
    assert hasattr(create_correct_triangle, 'area')


def test_check_triangle_add_area(create_correct_triangle, create_square):
    assert create_correct_triangle.add_area(create_square) == 106


def test_calculate_triangle_area(create_correct_triangle):
    assert round(create_correct_triangle.area, 2) == 6


def test_calculate_triangle_perimeter(create_correct_triangle):
    assert create_correct_triangle.perimeter == 12


def test_check_rectangle_has_name(create_rectangle):
    assert hasattr(create_rectangle, 'name')


def test_check_rectangle_has_perimeter(create_rectangle):
    assert hasattr(create_rectangle, 'perimeter')


def test_check_rectangle_has_area(create_rectangle):
    assert hasattr(create_rectangle, 'area')


def test_check_rectangle_add_area(create_rectangle, create_correct_triangle):
    assert create_rectangle.add_area(create_correct_triangle) == 16


def test_calculate_rectangle_area(create_rectangle):
    assert create_rectangle.area == 10


def test_calculate_rectangle_perimeter(create_rectangle):
    assert create_rectangle.perimeter == 14


def test_check_square_has_name(create_square):
    assert hasattr(create_square, 'name')


def test_check_square_has_perimeter(create_square):
    assert hasattr(create_square, 'perimeter')


def test_check_square_has_area(create_square):
    assert hasattr(create_square, 'area')


def test_check_square_add_area(create_square, create_circle):
    assert round(create_square.add_area(create_circle), 2) == 414.16


def test_calculate_square_area(create_square):
    assert create_square.area == 100


def test_calculate_square_perimeter(create_square):
    assert create_square.perimeter == 40


def test_check_circle_has_name(create_circle):
    assert hasattr(create_circle, 'name')


def test_check_circle_has_perimeter(create_circle):
    assert hasattr(create_circle, 'perimeter')


def test_check_circle_has_area(create_circle):
    assert hasattr(create_circle, 'area')


def test_check_circle_add_area(create_circle, create_rectangle):
    assert round(create_circle.add_area(create_rectangle), 2) == 324.16


def test_calculate_circle_area(create_circle):
    assert round(create_circle.area, 2) == 314.16


def test_calculate_circle_perimeter(create_circle):
    assert round(create_circle.perimeter, 2) == 62.83


def test_check_add_area_value_error(create_circle):
    with pytest.raises(ValueError):
        create_circle.add_area('lalala')
