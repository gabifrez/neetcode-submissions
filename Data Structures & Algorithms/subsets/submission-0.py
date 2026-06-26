class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curset = [], []
        if len(nums) == 0:
            return subsets
        def createSubsets(nums, i, curset, subsets):
            if i >= len(nums):
                subsets.append(curset.copy())
                return
            curset.append(nums[i])
            createSubsets(nums, i+1, curset, subsets)
            curset.pop()
            createSubsets(nums, i+1, curset, subsets)
        createSubsets(nums, 0, curset, subsets)
        return subsets