import pytest
from Equations import Equations


@pytest.mark.parametrize(
    'a, b, answer', [
        (1, 3, [-3]),
        (-5, 1, [0.2])
    ]
)
def test_linear(a, b, answer):
    assert Equations.linear(a, b) == answer


@pytest.mark.parametrize(
    'a, b, c, answer',
    [(1, -11, 28, [7, 4]),
     (4, -44, 121, [5.5, 5.5])]
)
def test_square(a, b, c, answer):
    assert Equations.square(a, b, c) == answer


@pytest.mark.parametrize(
    'a, b, c, d, answer',
    [(8, 12, 6, 1, [-0.5, -0.5, -0.5]),
     (8, -36, 54, -27, [1.5, 1.5, 1.5]),
     (1, 4, -3, -18, [2, -3, -3]),
     (1, -2, -16, 32, [-4, 4, 2]),
     (-1, -5, 4, 20, [-5, 2, -2])],
)
def test_cube(a, b, c, d, answer):
    assert Equations.cube(a, b, c, d) == answer


