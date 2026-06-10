class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right=len(nums)-1
        counter = 0
        if right == 0:
            return 0
        for i in range(len(nums)):
            if nums[i]==val:
                while nums[right]==val:
                    right-=1
                    if right == 0:
                        return counter
                nums[i]=nums[right]    
                right-=1
            else:    
                counter+=1
        return counter