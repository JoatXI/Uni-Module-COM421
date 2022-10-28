class queue:
    def __init__(self, capacity):
        self.internalArray = [None] * capacity
        self.front = 0
        self.next = 0
        self.queue_size = 0

    def add(self, data):
        self.internalArray[self.next] = data
        self.next += 1
        if len(self.internalArray) == self.next:
            self.next = 0

    def remove(self):
        self.internalArray[self.front] = None
        self.front += 1
        if len(self.internalArray) == self.front:
            self.front = 0
        return self.front

    def __str__(self,):
        return self.internalArray.__str__()

queue1 = queue(8)

queue1.add(1)
print(queue1)

queue1.add(2)
print(queue1)

queue1.add(3)
print(queue1)

queue1.add(4)
print(queue1)

queue1.add(5)
print(queue1)

queue1.add(6)
print(queue1)

queue1.add(7)
print(queue1)

queue1.add(8)
print(queue1)

