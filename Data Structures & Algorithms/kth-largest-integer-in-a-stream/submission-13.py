class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.heap = [0]
        for num in nums:
            self.heap.append(num)
            i = len(self.heap) - 1 
            if i > k:
                self.heap_pop()
            else:
                self.heap_add()
                
    def heap_pop(self): #stergere efectiva a elementului
        number = self.heap.pop()
        if number > self.heap[1]:
            self.heap[1] = number
        i = 1
        while 2 * i <= len(self.heap) - 1:
            if 2 * i + 1 <= len(self.heap) - 1 and self.heap[i*2 + 1] < self.heap[i*2]:
                temp = self.heap[i*2 + 1]
                self.heap[i*2 + 1] = self.heap[i]
                self.heap[i] = temp
                i = i*2+1
            elif self.heap[i*2] < self.heap[i]:
                temp = self.heap[i*2]
                self.heap[i*2] = self.heap[i]
                self.heap[i] = temp
                i*= 2
            else:
                break

    def heap_add(self):   #restructurare coada dupa ce am adaugat element
        i = len(self.heap) - 1
        while i > 1 and self.heap[i//2] > self.heap[i]:
            temp = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = temp
            i//=2
    def add(self, val: int) -> int:
        # return self.heap
        self.heap.append(val)
        self.heap_add()
        if(len(self.heap) - 1 > self.size):
            self.heap_pop()
        return self.heap[1]

        
