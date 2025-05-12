"""
Each node contains a distinct data value
The key values in the tree can be compared using "greater than" and "less than"
The key value of each node in the tree is less than every key value in its right subtree, and greater
than every key value in its left subtree
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if not self.root:
            self.root = node
            return self
        current = self.root
        while data != current.data:
            if data < current.data:
                if not current.left:
                    current.left = node
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    break
                current = current.right
        return self

