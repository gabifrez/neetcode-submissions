class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        history = {}
        result, left = 0, 0
        for right, element in enumerate(s):
            if element in history and history[element] >= left:
                left = history[element] + 1
            history[element] = right
            result = max(result, right - left + 1)
        return result