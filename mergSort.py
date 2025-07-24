# Divide and conquer
# sorts a list using the merge sort algorithm
# Complexity: Time - O(n*log n) Space - O(n)
import random


def merge_sort(arr):
    if len(arr) <= 1:  # base case / exit condition
        return arr

    # divide list into two halves
    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])

    # merge sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    # merges two sorted lists into a single sorted list
    result = []
    i = j = 0

    # compare elements from both lists and append smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # append any remaining elements from the left list
    while i < len(left):
        result.append(left[i])
        i += 1

    # append any remaining elements from the right list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# generate a pseudorandom 10 element list each time
my_list = []
for idx in range(0,10):
    my_list.append(random.randint(0, 100))

sorted_list = merge_sort(my_list)
print("Original list: ", my_list)
print("Sorted list: ", sorted_list)
