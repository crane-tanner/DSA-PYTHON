def bubble(a_list):
    for i in range(len(a_list)):
        has_swapped = False
        for j in range(1, len(a_list)):
            if a_list[j] < a_list[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
                has_swapped = True
        if not has_swapped:
            break
    return a_list


array = [6, 8, 1, 7, 0, -1]
print(bubble(array))

"""
inefficient for large arrays 
Time complexity: Best - O(n) Average - O(n^2) Worst - O(n^2)
Space complexity: O(1) 
"""