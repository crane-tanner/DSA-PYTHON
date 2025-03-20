# Computational complexity measures the amount of resources an algorithm requires to run
# "Big O" is the most commonly used notation for that


# O(1) Constant Time
"""
def function(list_of_numbers):
    select first number
    multiply by 2
    make it a string
    print it
O(1) algorithms take the same amount of effort to run,
regardless of the input size
Operations with constant complexity:
-simple variable assignments
-arithmetic operations and comparisons
-reference to a specific memory location (accessing elements in list by index or in a dictionary by key)
"""

# O(n) Linear Time
# def function(listofnumbers):
#   for num in listofnumbers:
#       change color to orange
# O(n) complexity indicates that the effort to run an algorithm grows proportionally
# to the amount of items being processed.


# O(n^2) Quadratic Time
# Algorithms running in quadratic time would do n^2 number of operations
# typically a loop within a loop is quadratic time
# for each in array:
#   for each in array:
#       do_something(of_constant_complexity)

# O(logn) Logarithmic time
# The logarithm is the inverse of the mathematical operation of exponentiation
# Example of O(nlogn)
# for each in array:
#   for only_a_few in array:
#       do_something(of_constant_complexity)

# Space Complexity: Auxiliary Space Complexity - The memory an algorithm needs to run, without counting the memory
# needed to store the input
# When creating new data inside an algorithm
# we need to think about the auxiliary memory utilization

# Asymptotic Complexity
# O(n^2 + 50n + 100) = O(n^2) (drop non-dominant terms and ignore constants)


