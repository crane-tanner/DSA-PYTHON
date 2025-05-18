def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key
    return array


new_list = [97, 101, 89, 99, 76, 65, 41, 30, 94]
insertion_sort(new_list)
print(new_list)
