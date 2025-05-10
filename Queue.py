# Queue is a FIFO data structure. First in, First out
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if not self.size:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return self

    def peek_tail(self):
        if self.size > 0:
            return self.tail.data
        else:
            return None

    def peak_head(self):
        if self.size > 0:
            return self.head.data
        else:
            return None

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def dequeue(self):
        if not self.size:
            raise Exception("queue is empty")
        former_head = self.head
        self.head = former_head.next
        former_head.next = None
        self.size -= 1
        if not self.size:
            self.tail = None
        return former_head.data


my_queue = Queue()
my_queue.enqueue(4)
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.dequeue()
print("Front of queue: ", my_queue.peek_tail())
print("Back of queue: ", my_queue.peak_head())
