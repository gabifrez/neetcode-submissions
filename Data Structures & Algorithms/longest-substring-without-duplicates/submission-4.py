class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        left, result, counter = 0, 0, 0
        viewed = set()
        for character in s:
            if character in viewed:
                result = max(result, counter)

                while True:
                    viewed.remove(s[left])
                    left += 1
                    counter -= 1
                    if s[left - 1] == character:
                        break
            counter += 1
            viewed.add(character)
        return max(result, counter)
