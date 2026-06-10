class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = temp = 0
        for num in nums:
            if num == 1:
                temp+=1
            else:
                mx = max(mx, temp)
                temp = 0
        mx = max(mx,temp)
        return mx;