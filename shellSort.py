def shell_sort(array):
    gaps = [3, 2, 1]
    for gap in gaps:
        for i in range(gap, len(array)):
            j = i - gap
            while array[j + gap] < array[j] and j >= 0:
                array[j], array[j+gap] = array[j+gap], array[j]
                j -= gap
    return array


my_list = [97, 101, 89, 99, 76, 65, 41, 30, 94]
print(shell_sort(my_list))

"""
Shell sort is basically insertion sort with extra steps 
Time complexity: Variable - depends on gaps and length of array 
Space complexity: O(1)
"""