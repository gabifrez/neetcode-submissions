class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.heapify(self.heap)

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.heapify(self.heap)
        return result

    def top(self) -> int:
        if len(self.heap) == 1:
            return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        if len(nums) == 0:
            return
        if nums[0] != 0:
            nums = [0] + nums
        l = len(nums) - 1
        length = l // 2
        while length > 0:
            i = length
            while 2 * i <= l:
                if 2*i + 1 <= l and nums[2*i + 1] < nums[2*i] and nums[i] > nums[2*i+1]:
                    temp = nums[i]
                    nums[i] = nums[2*i + 1]
                    nums[2*i + 1] = temp
                    i= i*2+1
                elif nums[i] > nums[2*i]:
                    temp = nums[i]
                    nums[i] = nums[2*i]
                    nums[2*i] = temp
                    i*= 2
                else:
                    break
            length -= 1
        self.heap = nums
        