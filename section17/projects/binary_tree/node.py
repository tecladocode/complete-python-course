class Node:
    def __init__(self, name, value, left=None, right=None):
        self.name = name
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'<Node {self.name}, {self.value}>'