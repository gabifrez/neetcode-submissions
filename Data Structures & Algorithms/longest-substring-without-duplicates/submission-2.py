class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxim, size, left = 0, 0, 0
        history = {}
        for character in s:
            if character in history:
                if size > maxim:
                    maxim = size
                while s[left] != character:
                    del history[s[left]]
                    size -= 1
                    left += 1
                del history[s[left]]
                size -= 1
                left += 1
            if character not in history:
                history[character] = 1
                size += 1
        return max(maxim,size)
            