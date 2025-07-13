
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def dft_post_order_iterative(self):
        if not self.root:
            raise Exception('Empty tree')
        current = previous = self.root
        stack = []
        visited = []
        while current:
            while current.left:
                stack.append(current)
                current = current.left
            while not current.right or current.right == previous:
                visited.append(current.data)
                previous = current
                if not stack:
                    return visited
                current = stack.pop()
            stack.append(current)
            current = current.right
        return visited


