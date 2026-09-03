class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result, counter, total, left = len(nums), 0, 0, 0
        for right in range(len(nums)):
            total += nums[right]
            counter += 1
            while total >= target:
                total -= nums[left]
                left += 1
                result = min(result , counter)
                counter -= 1
        return 0 if sum(nums) < target else result
                
