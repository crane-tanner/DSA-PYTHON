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
    return fib(n - 1) + fib(n - 2)


array = [6, 4, 5, 2, 8, 1]


# Example of an iterative function
def multiply_arr(arr):
    total = 1
    for n in arr:
        total *= n
    return total


# Recursive version
def array_product(arr):
    if not arr:
        return 1
    return arr[0] * array_product(arr[1:])


print(array_product(array))
print(multiply_arr(array))
print(fib(10))
print(factorial(1))

# What to consider if determining complexity of recursive functions
# the number of stack frames
# the number of recursive calls
# The other operations done inside the function
# the space complexity (the max number of stack frames)
