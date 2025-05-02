class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        if not self.length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return self

    def pop_left(self):
        if not self.length:
            raise Exception("list is empty")
        former_head = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = former_head.next
            former_head.next = None
            self.head.prev = None
        self.length -= 1
        return self

    def pop_right(self):
        if not self.length:
            raise Exception("list is empty")
        former_tail = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = former_tail.prev
            former_tail.prev = None
            self.tail.next = None
        self.length -= 1
        return former_tail.value

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
            return self.pop_right()
        current_node.next.prev = prev_node
        prev_node.next = current_node.next
        current_node.prev = None
        current_node.next = None
        self.length -= 1
        return current_node.value


my_list = DoublyLinkedList()
my_list.append(2)
my_list.append(3)
my_list.prepend(1)
my_list.append(4)

my_list.remove(1)

print(my_list)
print("Head value:", my_list.head.value)
print("Tail value:", my_list.tail.value)
print("Length:", my_list.length)
