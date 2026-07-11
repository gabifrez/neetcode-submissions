class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i])
        postfix = [0] * len(nums)
        postfix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        result = [postfix[1]]
        for i in range(1,len(nums) - 1):
            result.append(postfix[i+1] * prefix[i-1])
        result.append(prefix[-2])
        return result