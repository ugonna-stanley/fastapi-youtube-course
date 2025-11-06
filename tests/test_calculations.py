import pytest
from app.calculations import add

@pytest.mark.parametrize("num1, num2, expected",[
    (3, 5, 8),
    (4, 9, 13),
    (102, 204, 306)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected