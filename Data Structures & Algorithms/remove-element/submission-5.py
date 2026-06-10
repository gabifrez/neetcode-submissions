class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        right = len(nums)
        while i < right:
            if nums[i] == val:
                right-=1
                nums[i] = nums[right]
            else:
                i+=1
        return right