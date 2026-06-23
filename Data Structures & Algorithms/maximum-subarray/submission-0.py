class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, current_sum = nums[0], 0
        for element in nums:
            current_sum = max(current_sum, 0)
            current_sum += element
            max_sum = max(current_sum, max_sum)
        return max_sum