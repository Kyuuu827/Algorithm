# Queue 구현
class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        if not self.queue:
            return True
        else:
            return False

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            dequeued = self.queue[0]
            self.queue = self.queue[1:]
            return dequeued

    def print(self):
        return print(self.queue)

queue = Queue()
print(queue.isEmpty())
queue.enqueue(1)
print(queue.print()) 
queue.dequeue()
print(queue.print())