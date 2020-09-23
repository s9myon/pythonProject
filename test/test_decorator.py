import pytest
from decorator import pow, square


@pytest.mark.parametrize(
    'a, answer',
    [(9, 81)]
)
def test_square(a, answer):
    @square
    def f(x):
        return x
    assert f(a) == answer


@pytest.mark.parametrize(
    'p, a, b, c, answer',
    [(6, 3, 4, 10, 64)]
)
def test_power(p, a, b, c, answer):
    @pow(power=p)
    def f(x, y, z):
        return x * y - z
    assert f(a, b, c) == answer
