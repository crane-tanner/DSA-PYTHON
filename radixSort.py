import math

def radix_sort(array):
    max_digits = get_max_number_of_digits(array)
    for i in range(max_digits + 1):
        buckets = [[] for _ in range(10)]
        for num in array:
            digit = get_digit_at_position(num, position=i)
            buckets[digit].append(num)
        array = flatten(buckets)
    return array

def get_max_number_of_digits(array):
    return max(int(math.log10(abs(num))) + 1 if num != 0 else 1 for num in array)

def get_digit_at_position(number, position):
    return (abs(number) // 10 ** position) % 10

def flatten(array):
    return [num for inner in array for num in inner]


numbers = [32, 1, 3462, 634774, 21]
print("Sorted array:", radix_sort(numbers))

# Time and Space Complexity: O(nk) and O(n + k)
