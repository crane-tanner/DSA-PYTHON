# Divide and conquer
# sorts a list using the merge sort algorithm
def merge_sort(arr):
    if len(arr) <= 1:  # base case
        return arr

    # divide list into two halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # recursively sort both halves

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

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


my_list = [2, 4, 1, 6, 5, 3, 8, 7]
sorted_list = merge_sort(my_list)
print("Original list: ", my_list)
print("Sorted list: ", sorted_list)
