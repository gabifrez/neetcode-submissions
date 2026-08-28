class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim = current = nums[0]
        current -= nums[0]
        for num in nums:
            current+= num
            maxim = max(maxim, current)
            if current < 0:
                current = 0
        return maxim