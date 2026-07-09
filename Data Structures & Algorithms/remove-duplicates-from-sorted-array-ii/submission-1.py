class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        flag = 1
        for i in range(1, len(nums)): 
            if nums[i] == nums[i-1]:
                flag +=1
                if flag <=2:
                    nums[left] = nums[i]
                    left+=1
        
            if nums[i] != nums[i-1]:
                nums[left] = nums[i]
                left +=1
                flag = 1

    
        return left