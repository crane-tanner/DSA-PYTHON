
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def dft_in_order_iterative(self):
        if not self.root:
            raise Exception('Empty tree')
        current_node = self.root
        stack = []
        visited = []
        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                visited_node = stack.pop()
                visited.append(visited_node)
                if not visited_node.right:
                    continue
                current_node = current_node.right
        return visited


# Time and Space complexity O(n)