class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for number in nums:
            total += number
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
        