"""
A prime factor generator.
"""
import sys

factors = []

def generate_prime_factors(number, factors):
    """
    Step 1: Accepts an integer parameter, and returns a
            list of integers from that function.
    """
    if (type(number) is not int):
        raise ValueError
