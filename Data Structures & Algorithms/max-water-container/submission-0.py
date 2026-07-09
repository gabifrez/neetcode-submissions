class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights) - 1
        left = 0
        right = length
        maxarea = 0
        while left < right:
            maxarea = max(min(heights[left],heights[right]) * length, maxarea)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            length -=1
        return maxarea