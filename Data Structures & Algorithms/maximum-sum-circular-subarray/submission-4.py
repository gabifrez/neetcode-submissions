class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, curMin, curMax, globMin, globMax = 0, 0, 0, nums[0], nums[0]
        
        for num in nums:
            curMin = min(curMin + num, num)
            curMax = max(curMax + num, num)
            globMin = min(curMin, globMin)
            globMax = max(curMax, globMax)
            total += num

        return max(total - globMin, globMax) if globMax > 0 else globMax