class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop() if self.items else None

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())