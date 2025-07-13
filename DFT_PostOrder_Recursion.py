
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def dft_postorder_recursion(self):
        if not self.root:
            raise Exception('Empty tree')
        visited = []

        def _traverse(node):
            if node:
                _traverse(node.left)
                _traverse(node.right)
                visited.append(node.data)
            return

        _traverse(self.root)
        return visited

