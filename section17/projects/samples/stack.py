class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, e):
        self.items = [e] + self.items
    
    def pop(self):
        return self.items.pop()


s = Stack()
s.push(5)  # [5]
s.push(7)  # [7, 5]
s.push(11)  # [11, 7, 5]
print(s.pop())  # returns 11, left is [7, 5]
print(s.pop())  # returns 7, left is [5]