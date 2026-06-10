class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        temp=0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                temp+=1;
            if nums[i] == 0 or i==len(nums)-1:
                if temp >= mx:
                    mx = temp;
                temp=0
        return mx;