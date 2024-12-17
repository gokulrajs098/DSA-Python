from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque([])
    
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            self.queue.popleft()
        else:
            return "Queue is empty"
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"
        
    def is_empty(self):
        return len(self.queue) == 0

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()

print(queue.front())
print(queue.is_empty())