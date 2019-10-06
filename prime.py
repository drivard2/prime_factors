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
        while i <= number:
            # If the number can be divided evenly with no remainder (modulus),
            # append the iterator to the list of factors:
            if (number % i) == 0:
                factors.append(i)

                # To prevent infinite loop, assign a decreased value to number
                # by dividing itself with the current iterator:
                number /= i
            else:
                # To test for values higher than 2, iterate i by 1 each time
                # through the loop. Satisfies conditions of test_param_three
                # in addition to needing a loop:
                i += 1

        return factors
