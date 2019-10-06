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
    else:
        # Instantiate iterator to 2. Satisfies conditions of test_param_one
        # and test_param_two (Value must be at least 2)
        i = 2
            # If the number can be divided evenly with no remainder (modulus),
            # append the iterator to the list of factors:
        if (number % i) == 0:
            factors.append(i)

        return factors
