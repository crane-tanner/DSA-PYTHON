# Last in, first out (LIFO) Data Structure
# Array implementation
stack = []
stack.append(2)
stack.append(56)
stack.append(3)

while len(stack) > 0:
    stack.pop()

print(stack)


# Linked List implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size =
        self.max_size = 100

    def __len__(self):
        return self.size

    def push(self, data):
        if self.max_size == self.size:
            raise Exception("stack size limit reached")
        new_element = Node(data)
        new_element.next = self.top
        self.top = new_element
        self.size += 1
        return self

    def pop(self):
        if not self.size:
            raise Exception("stack is empty")
        former_top = self.top
        self.top = former_top.next
        former_top.next = None
        self.size -= 1
        return former_top.data

    def peek(self):
        return self.top.data if self.top else None

    def clear(self):
        self.top = None
        self.size = 0
        return self


my_stack = Stack()
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack.__len__())
my_stack.clear()

print(my_stack.peek())
