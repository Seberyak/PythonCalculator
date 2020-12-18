import pytest
import calc


def test_split():
    assert calc.split("1+4/4") == [1, '+', 4, '/', 4]
    assert calc.split("4*5/2+12-26") == [4, '*', 5, '/', 2, '+', 12, '-', 26]


def test_calculate():
    assert calc.calculate(1, '*', 3) == 1 * 3
    assert calc.calculate(1, '+', 3) == 1 + 3
    assert calc.calculate(1, '-', 3) == 1 - 3
    assert calc.calculate(1, '/', 3) == 1 / 3
    with pytest.raises(ZeroDivisionError):
        assert calc.calculate(1, '/', 0)


def test_ordering():
    assert calc.ordering_operations([1, '+', 3, '*', 4, '/', 2]) == 7
    assert calc.ordering_operations([1, '+', 3, '*', 4, '/', 2, '-', 7]) == 0
    with pytest.raises(ZeroDivisionError):
        assert calc.ordering_operations([5, '-', 10, '/', 5, '*', 0])
    with pytest.raises(IndexError):
        assert calc.ordering_operations([])
    with pytest.raises(AssertionError):
        assert calc.ordering_operations([4, '%', 0])
