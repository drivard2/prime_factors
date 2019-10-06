"""
Tests the generate_prime_factors function
"""

import pytest
from prime import generate_prime_factors


def test_integer():
    """
    STEP 1: Given anything but an integer value, a ValueError should be raised.
    appended.
    """
    factors = []
    value_types = [ "abcd1234", 2.54, 3.14J ]

    for value in value_types:
        with pytest.raises(ValueError):
            generate_prime_factors(value, factors)


def test_param_one():
    """
    STEP 2: Given 1 as a parameter, an empty list should be returned.
    """
    factors = []
    value = 1

    assert len(generate_prime_factors(value, factors)) == 0


def test_param_two():
    """
    STEP 3: Given 2 as a parameter, a list containing one value of
    2 should be returned.
    """
    factors = []
    value = 2
    output_list = generate_prime_factors(value,factors)

    assert len(output_list) == 1 and output_list[0] == 2
