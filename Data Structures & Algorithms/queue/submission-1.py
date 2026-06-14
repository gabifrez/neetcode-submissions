class Node:
    def __init__(self, prev=None, val=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next

class Deque:
    
    def __init__(self):
       self.queue = Node()
       self.tail = self.queue
       self.counter = 0

    def isEmpty(self) -> bool:
        return self.counter == 0

    def append(self, value: int) -> None:
        node = Node(prev = self.tail, val = value)
        self.tail.next = node
        self.tail = self.tail.next
        if self.isEmpty():
            self.tail.prev = None
            self.queue = self.tail
        self.counter += 1

    def appendleft(self, value: int) -> None:
        node = Node(val = value, next = self.queue)
        self.queue.prev = node
        self.queue = self.queue.prev
        if self.isEmpty():
            self.queue.next = None
            self.tail = self.queue
        self.counter += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        self.counter -=1
        eliminated = self.tail.val
        if self.isEmpty():
            self.queue = self.tail = Node()
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return eliminated
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        self.counter -=1
        eliminated = self.queue.val
        if self.isEmpty():
            self.queue = self.tail = Node()
        else:
            self.queue = self.queue.next
            self.queue.prev = None
        return eliminated
       
