class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        if not self.length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self


new_list = SinglyLinkedList()
new_list.append(3)
new_list.append(5)
new_list.append(19)
new_list.prepend(1)

print(new_list)
print("Head value: ", new_list.head.value)
print("Tail value: ", new_list.tail.value)
print("Length: ", new_list.length)
