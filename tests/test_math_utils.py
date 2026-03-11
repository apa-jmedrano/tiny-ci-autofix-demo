import pytest

from math_utils import add, is_even, safe_divide


def test_add_small_numbers() -> None:
    assert add(2, 3) == 5


def test_safe_divide() -> None:
    assert safe_divide(9, 3) == 3


def test_safe_divide_by_zero_raises() -> None:
    with pytest.raises(ValueError):
        safe_divide(1, 0)


def test_is_even() -> None:
    assert is_even(10) is True
    assert is_even(11) is False
