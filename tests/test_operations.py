import pytest
from app.operations import addition, subtraction, multiplication, division

#parametrized yay
@pytest.mark.parametrize("func,a,b,expected", [
    (addition, 1, 1, 2),
    (subtraction, 1, 1, 0),
    (multiplication, 2, 3, 6),
    (division, 6, 2, 3),
])
def test_operations(func, a, b, expected):
    assert func(a, b) == expected


def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)