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
        #instantiate iterator to 2. Satisfies condition of test_param_one
        i = 2
            # If the number can be divided evenly with no remainder (modulus),
            # append the iterator to the list of factors:
        if (number % i) == 0:
            factors.append(i)

        return factors
