import math
import random

n = random.randint(10, 1000)


def print_digits(param):
    if param >= 10:
        print(math.trunc(param / 10))
        print_digits(param / 10)
    return math.trunc(param)


print_digits(n)
