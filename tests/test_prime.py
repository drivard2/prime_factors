"""
Tests the generate_prime_factors function
"""

import pytest
from prime import generate_prime_factors


def test_integer():
    """
    Given anything but an integer value, a ValueError should be raised.
    appended.
    """
    factors = []
    value_types = [ "abcd1234", 2.54, 3.14J ]

    for value in value_types:
        with pytest.raises(ValueError):
            generate_prime_factors(value, factors)
