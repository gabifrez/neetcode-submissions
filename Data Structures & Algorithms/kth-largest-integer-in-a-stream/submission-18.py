class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.heap = [0]
        for num in nums:
            if len(self.heap) - 1 < k:
                self.heap_add(num)
            elif self.heap[1] < num:
                self.heap.append(num)
                self.heap_pop()
                
    def heap_pop(self): #stergere efectiva a elementului
        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i <= len(self.heap) - 1:
            if 2 * i + 1 <= len(self.heap) - 1 and self.heap[i*2 + 1] < self.heap[i*2] and self.heap[i] > self.heap[i*2 + 1]:
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
    def heap_add(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i//2] > self.heap[i]:
            temp = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = temp
            i//=2
    
    def add(self, val: int) -> int:
        # daca coada nu e plina
        if len(self.heap) - 1 < self.size:
            self.heap_add(val)
        # e plina dar acum trebuie sa verificam daca adaugam elementul
        elif val > self.heap[1]:
            self.heap.append(val)
            self.heap_pop()
        return self.heap[1]

        
