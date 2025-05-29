def selection_sort(array):
    for idx in range(len(array)):
        smallest = idx
        for idx2 in range(idx+1, len(array)):
            if array[idx2] < array[smallest]:
                smallest = idx2
        array[idx], array[smallest] = array[smallest], array[idx]
    return array

new_arr = [8, 2, 7, 1, 5]
print(selection_sort(new_arr))


"""
Inefficient for large arrays
Time complexity - Best: O(n^2) Average: O(n^2) Worst: O(n^2) 
Space complexity: O(1)
"""