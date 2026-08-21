class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        index = 0
        while len(queue) < k:
            heapq.heappush(queue, nums[index])
            index+=1
        for i in range(index, len(nums)):
            if nums[i] > queue[0]:
                heapq.heappop(queue)
                heapq.heappush(queue, nums[i])
        return queue[0]