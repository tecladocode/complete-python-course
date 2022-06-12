class Stack:
    def __init__(self):
        self.items = []

    def push(self, e):
        self.items = [e] + self.items

    def pop(self):
        return self.items.pop(0)