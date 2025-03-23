# Recursion is a method of solving a problem
# where the solution is defined in terms of a smaller version of itself
# It is essentially a function that calls itself

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(10))
print(factorial(1))

# Classic examples of recursion problems
