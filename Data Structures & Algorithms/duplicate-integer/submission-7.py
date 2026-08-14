class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        indexing = {}
        for num in nums:
            if num not in indexing:
                indexing[num] = 1
            else:
                return True
        return False