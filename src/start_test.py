from .start import soma


def test_soma():
    """Testing start.py/soma"""

    result = soma(2, 4)
    assert result == 6


def test_soma_negative_numbers():
    """Testing start.py/soma with negative numbers"""

    result = soma(-5, -9)
    assert result == -14
