class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, e):
        self.items = [e] + self.items
    
    def pop(self):
        return self.items.pop(0)


s = Stack()
s.push(5)       # [5]
s.push(7)       # [5, 7]
s.push(11)      # [5, 7, 11]
print(s.pop())  # returns 11, left is [5, 7]
print(s.pop())  # returns 7, left is [5]
