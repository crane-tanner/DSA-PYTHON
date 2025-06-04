def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


new_list = [97, 101, 89, 0, 94]
print("Before:", new_list)
print("After:", insertion_sort(new_list))

"""
Insertion sort best for smaller datasets or arrays 
Time complexity - Best: O(n), Average: O(n^2), Worst: O(n^2)
Space complexity - O(1) 
"""