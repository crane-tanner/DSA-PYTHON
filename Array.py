# Arrays are known as Lists in Python
def add_elements(arr):
    total = 0
    for num in my_list:
        total += num
    print("Sum of all numbers in list:", total)


my_list = [3, 9, 12, 15, 20]
my_list.insert(3, 0)
my_list.pop()

add_elements(my_list)
print(my_list)

# Big O of lists
# adding to the end O(1)
# removing from the end O(1)
# inserting at the beginning O(n)
# removing from the beginning O(n)
# inserting and removing from within O(n)
# accessing by index 0(1)
