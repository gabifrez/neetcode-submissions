class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for index,number in enumerate(nums):
            if number > 0:
                break
            if index > 0 and number == nums[index - 1]:
                continue
            
            left, right = index + 1, len(nums) - 1
            while left < right:
                tSum = number + nums[left] + nums[right]
                if tSum > 0:
                    right -= 1
                elif tSum < 0:
                    left += 1
                else:
                    res.append([number, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left +=1
        return res

        

