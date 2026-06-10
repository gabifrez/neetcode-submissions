class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = {}
        for element in nums:
            if element not in values:
                values[element] = 1
            else:
                return True
        return False
         