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


class BinarySearchTree:
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

    def contains(self, data):
        if not self.root:
            return False
        current = self.root
        while data != current.data:
            if data < current.data:
                if not current.left:
                    return False
                current = current.left
            elif data > current.data:
                if not current.right:
                    return False
                current = current.right
            else:
                return True
        return "Node found containing: " + str(data)

    def remove(self, data, start=None, parent=None):
        current = start or self.root
        while current and current.data != data:
            parent = current
            if data < current.data:
                current = parent.left
            else:
                current = parent.right
        if not current:
            raise Exception("node not found")
        if not current.left and not current.right:
            return self._remove_node_no_children(current, parent)
        if current.right and current.left:
            return self._remove_node_two_children(current)
        return self._remove_node_one_child(current, parent)

    def _remove_node_no_children(self, current, parent):
        if current is self.root:
            self.root = None
            return self
        if parent.left == current:
            parent.left = None
        else:
            parent.right = None
        return self

    def _remove_node_one_child(self, current, parent):
        if current is self.root:
            self.root = current if current.right else current.left
            return self
        if parent.right == current:
            parent.right = current.right if current.right else current.left
        else:
            parent.left = current.right if current.right else current.left
        return self

    def _remove_node_two_children(self, current):
        successor = self._get_successor(current)
        current.data = successor.data
        return self.remove(successor, start=current.right, parent=current)

    @staticmethod   # grouping related functionality within a class without tying it to the class's state.
    def _get_successor(current):
        successor = current.right
        while successor and successor.left:
            successor = current.left
        return successor


new_tree = BinarySearchTree()
new_tree.insert(4)
new_tree.insert(2)
new_tree.insert(3)
new_tree.insert(7)
new_tree.remove(3)
print(new_tree)
print(new_tree.contains(3))
