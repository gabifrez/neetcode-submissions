class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets, curset = [], []
        if len(nums) == 0:
            return subsets
        nums.sort()

        def subset(index, nums, curset, subsets):
            if index >= len(nums):
                subsets.append(curset.copy())
                return
            
            curset.append(nums[index])
            subset(index + 1, nums, curset, subsets)

            curset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            subset(index + 1, nums, curset, subsets)

        subset(0, nums, curset, subsets)
        return subsets