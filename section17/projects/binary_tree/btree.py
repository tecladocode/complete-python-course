from node import Node

class BinaryTree:
    def __init__(self, head: Node):
        self.head = head
    
    def add(self, node: Node):
        current_node = self.head
        while current_node:
            if node.value == current_node.value:
                raise ValueError("A node with that value already exists.")
            elif node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = node
                    break
            else:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = node
                    break
    
    def find(self, value: int):
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        raise LookupError("A node with value {} was not found.".format(value))
    
    def flatten(self):
        self._flatten_recursive(self.head)
    
    def _flatten_recursive(self, current_node):
        if not current_node:
            return
        self._flatten_recursive(current_node.left)
        print(current_node)
        self._flatten_recursive(current_node.right)
        