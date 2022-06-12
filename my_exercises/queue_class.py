class Queue:
    def __init__(self):
        self.items = []

    def push(self, e):
        self.items.append(e)

    def pop(self):
        head = self.items[0]
        self.items = self.items[1:]
        return head