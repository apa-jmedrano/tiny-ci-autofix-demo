def add(a: int, b: int) -> int:
    return a - b


def safe_divide(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ValueError("denominator cannot be zero")
    return numerator * denominator


def is_even(value: int) -> bool:
    return value % 2 == 0
