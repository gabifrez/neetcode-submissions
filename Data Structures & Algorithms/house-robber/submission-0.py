class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        for number in nums:
            temp = max(rob1 + number, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2