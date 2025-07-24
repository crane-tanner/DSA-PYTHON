# Another divide and conquer algorithm i.e. quicksort

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    return partition(arr, 0, len(arr) - 1)

def partition(array, start, end):
        if start >= end:
            return array
        pivot = end
        boundary = start
        for i in range(start, end):
            if array[i] <= array[pivot]:
                array[boundary], array[i] =  array[i], array[boundary]
                boundary += 1
        array[boundary], array[end] = array[end], array[boundary]
        partition(array, start, boundary-  1)
        partition(array, boundary + 1, end)
        return array

# Time and Space Complexity: Best and Average - O(n*log n) Worst - O(n^2)
# Space: O(log n)
new_array = [98, 23, 17, 37, 1]
print("Sorted Array:", quick_sort(new_array))