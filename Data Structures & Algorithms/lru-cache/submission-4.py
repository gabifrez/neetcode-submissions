class Node:
    def __init__(self, key= None,  val=None, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.first = self.last = Node()
        self.first.next = self.last
        self.last.prev = self.first
      
    def remove(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left

    def append(self, node):
        left_node = self.last.prev
        right_node = self.last
        left_node.next = right_node.prev = node
        node.prev = left_node
        node.next = right_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        #remove the node conextions from the list
        self.remove(node)
        #append the last one
        self.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # if the key in cache remove and append at the end
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.append(node)
            return
        
        if self.size:
            self.size -= 1
            node = Node(val = value, key = key)
            self.append(node)
            self.cache[key] = node
        else:
            node = self.first.next
            self.first.next = node.next
            node.next.prev = self.first
            self.remove(node)
            del self.cache[node.key]
            #append the new one
            nnode = Node(val = value, key = key)
            self.append(nnode)
            self.cache[key] = nnode
            

        
