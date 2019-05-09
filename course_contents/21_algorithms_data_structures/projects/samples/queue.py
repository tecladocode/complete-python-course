class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, e):
        self.items.append(e)
    
    def pop(self):
        head = self.items[0]
        self.items = self.items[1:]
        return head

q = Queue()
q.push(5)  # [5]
q.push(7)  # [5, 7]
q.push(11)  # [5, 7, 11]
print(q.pop())  # returns 5, left is [7, 11]
print(q.pop())  # returns 7, left is [11]
