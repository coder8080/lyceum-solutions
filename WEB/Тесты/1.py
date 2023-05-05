from yandex_testing_lesson import Rectangle
import pytest


def test_Rectangle():
    # Неправильные аргументы
    with pytest.raises(TypeError):
        r = Rectangle('2', 1)
    with pytest.raises(TypeError):
        r = Rectangle(1, '2')
    with pytest.raises(TypeError):
        r = Rectangle('22', '2')
    with pytest.raises(TypeError):
        r = Rectangle(['2', '2'], 2)
    with pytest.raises(TypeError):
        r = Rectangle(4, ['3', '3'])
    with pytest.raises(TypeError):
        r = Rectangle(['5', '2'], ['66', '4'])
    with pytest.raises(TypeError):
        r = Rectangle(['2', '7'], ['8', '9'])
    with pytest.raises(ValueError):
        r = Rectangle(-2, 40)
    with pytest.raises(ValueError):
        r = Rectangle(40, -2)
    with pytest.raises(ValueError):
        r = Rectangle(-4, -4)

    # Налчие методов
    r = Rectangle(4, 4)
    assert hasattr(r, 'get_area')
    assert hasattr(r, 'get_perimeter')

    r = Rectangle(8, 9)
    assert hasattr(r, 'get_area')
    assert hasattr(r, 'get_perimeter')

    # get_area
    r = Rectangle(4, 4)
    assert r.get_area() == 16
    r = Rectangle(8, 9)
    assert r.get_area() == 8 * 9
    r = Rectangle(1, 2)
    assert r.get_area() == 2
    r = Rectangle(1, 1)
    assert r.get_area() == 1
    r = Rectangle(0, 1)
    assert r.get_area() == 0
    r = Rectangle(1, 0)
    assert r.get_area() == 0
    r = Rectangle(0, 0)
    assert r.get_area() == 0

    # get_perimeter
    r = Rectangle(1, 1)
    assert r.get_perimeter() == 4
    r = Rectangle(8, 9)
    assert r.get_perimeter() == 16 + 18
    r = Rectangle(0, 0)
    assert r.get_perimeter() == 0
    r = Rectangle(0, 1)
    assert r.get_perimeter() == 2
    r = Rectangle(1, 0)
    assert r.get_perimeter() == 2
