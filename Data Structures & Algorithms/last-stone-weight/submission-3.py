class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            result = (heapq.heappop(heap) - heapq.heappop(heap))
            if result:
                heapq.heappush(heap, result)
        return 0 if not len(heap) else -heap[0]

