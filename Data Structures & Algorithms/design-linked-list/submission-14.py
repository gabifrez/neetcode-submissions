class Node:
    def __init__(self, prev=None, val=None, next=None):
        self.prev = prev
        self.val =  val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.MyList = Node('')
        self.head = Node('')
        self.tail = Node('')
        self.n = 0

    def to_index(self, index: int) -> Node:
        i=0
        head = self.MyList
        while index > i:
            head = head.next
            i+=1
        return head

    def get(self, index: int) -> int:
        if index >= self.n:
            return -1
        return (self.to_index(index)).val

    def addAtHead(self, val: int) -> None:
        self.head = Node(val=val, next=self.MyList)
        self.MyList.prev = self.head
        self.MyList = self.head
        if self.n == 0:
            self.MyList.next = None
            self.tail = self.MyList
        self.n += 1

    def addAtTail(self, val: int) -> None:
        self.tail.next = Node(prev = self.tail, val=val)
        self.tail = self.tail.next
        if self.n == 0:
            self.tail.prev = None
            self.MyList = self.head = self.tail
        self.n += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.n:
            return
        elif self.n == index:
            self.addAtTail(val)
        elif self.n == 0:
            self.addAtHead(val)
        else:
            head = self.to_index(index)
            node = Node(prev = head.prev, val=val, next = head)
            node.prev.next = node
            node.next.prev = node
            self.n += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.n:
            return
        else:
            if index == 0:
                self.head = self.head.next
                if self.head == self.tail:
                    self.head.next = self.tail.prev = None
                if self.head == None:
                    self.head = self.tail = self.MyList = Node()
            elif index == self.n - 1:
                self.tail = self.tail.prev
                if self.tail == self.head:
                    self.head.next = self.tail.prev
                if self.tail == None:
                    self.tail = self.head = self.MyList = Node()
            else:
                current = self.to_index(index)
                current.prev.next = current.next
                current.next.prev = current.prev
            self.n -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)