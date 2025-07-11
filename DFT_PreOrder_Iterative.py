
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def dft_preorder_iterative(self):
        if not self.root:
            raise Exception('Empty tree')
        stack = [self.root]
        visited = []
        while stack:
            visited_node = stack.pop()
            visited.append(visited_node.data)
            if visited_node.left:
                stack.append(visited_node.left)
            if visited_node.right:
                stack.append(visited_node.right)
        return visited

# Time & Space complexity both O(n)

BST = BinarySearchTree()
print(BST.dft_preorder_iterative())