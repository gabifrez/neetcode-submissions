class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i//2 > 0:
            if self.heap[i//2] > self.heap[i]:
                temp = self.heap[i//2]
                self.heap[i//2] = self.heap[i]
                self.heap[i] = temp
                i//= 2
            else:
                break

    def pop(self) -> int:
        if len(self.heap) < 2:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2*i < len(self.heap):
            if 2*i + 1 < len(self.heap) and self.heap[2*i+1] < self.heap[2*i] and self.heap[2*i+1] < self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[2*i + 1]
                self.heap[2*i + 1] = temp
                i= i*2 + 1
            elif self.heap[2*i] < self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[2*i]
                self.heap[2*i] = temp
                i= i*2
            else:
                break
        return result

    def top(self) -> int:
        if len(self.heap) < 2:
            return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        if len(nums) == 0:
            return
        self.heap = [0] + nums

        l = len(self.heap) - 1
        length = l // 2
        while length > 0:
            i = length
            while 2 * i <= l:
                if 2*i + 1 <= l and self.heap[2*i + 1] < self.heap[2*i] and self.heap[i] > self.heap[2*i+1]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2*i + 1]
                    self.heap[2*i + 1] = temp
                    i= i*2+1
                elif self.heap[i] > self.heap[2*i]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2*i]
                    self.heap[2*i] = temp
                    i*= 2
                else:
                    break
            length -= 1
        
        
        