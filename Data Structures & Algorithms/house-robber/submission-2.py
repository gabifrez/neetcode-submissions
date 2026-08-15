class Solution:
    def rob(self, nums: List[int]) -> int:
        tmp1 = tmp2 = 0
        for num in nums:
            temp = max(tmp1 + num, tmp2)
            tmp1 = tmp2
            tmp2 = temp
        return tmp2