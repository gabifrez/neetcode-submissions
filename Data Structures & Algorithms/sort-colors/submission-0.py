class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors_counter = [0,0,0]
        for color in nums:
            colors_counter[color] += 1
        nums[:colors_counter[0]] = [0] * colors_counter[0]
        nums[colors_counter[0]:colors_counter[1]+ colors_counter[0]] = [1] * colors_counter[1]
        nums[colors_counter[1]+ colors_counter[0]:colors_counter[1]+ colors_counter[0] + colors_counter[2]] = [2] * colors_counter[2]

        