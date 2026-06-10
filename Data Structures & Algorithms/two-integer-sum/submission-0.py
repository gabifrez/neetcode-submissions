class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        start, end = 0, 0
        for i in range(len(nums)):
            result = target - nums[i]
            if result in counter:
                start = counter[result]
                end = i
            else:
                counter[nums[i]] = i
        return [start, end]

        