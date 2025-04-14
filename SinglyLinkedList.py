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

    def pop_left(self):
        if not self.length:
            raise Exception("list is empty")
        former_head = self.head
        self.head = former_head.next
        former_head.next = None
        self.length -= 1
        if not self.length:
            self.tail = None
        return former_head.value

    def pop_right(self):
        if not self.length:
            raise Exception("list is empty")
        tail_value = self.tail.value
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = None
        self.length -= 1
        return tail_value

    def remove(self, value):
        if not self.length:
            raise Exception("list is empty")
        if self.head.value == value:
            return self.pop_left()
        prev_node = self.head
        current_node = self.head.next
        while current_node is not None and current_node.value != value:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            raise Exception("item not in the list")
        if current_node.next is None:
            self.tail = prev_node
        prev_node.next = current_node.next
        current_node.next = None
        self.length -= 1
        return current_node.value


new_list = SinglyLinkedList()
new_list.append(5)
new_list.append(6)
new_list.append(7)
new_list.prepend(3)
new_list.prepend(2)
print(new_list.remove(5))

print(new_list)
print("Head value:", new_list.head.value)
print("Tail value:", new_list.tail.value)
print("Length:", new_list.length)
