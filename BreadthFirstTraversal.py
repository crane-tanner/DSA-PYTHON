from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def breadth_first_traversal(self):
        if not self.root:
            raise Exception('Empty tree')
        queue = deque()
        queue.append(self.root)
        visited = []
        while queue:
            visited_node = queue.popleft()
            visited.append(visited_node.data)
            if visited_node.left:
                visited.append(visited_node.left)
            if visited_node.right:
                visited.append(visited_node.right)
        return visited
"""
Breadth first traversal time complexity: O(n)
Space complexity: O(n) 
"""


BST = BinarySearchTree()
print(BST.breadth_first_traversal())