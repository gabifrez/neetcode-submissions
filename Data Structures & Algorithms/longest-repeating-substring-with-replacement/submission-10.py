class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result, left = 0, 0
        maxf = 0
        dictionary = {}
        for i in range(len(s)):
            dictionary[s[i]] = 1 + dictionary.get(s[i], 0)
            maxf = max(maxf, dictionary[s[i]])
            while (i - left + 1) - maxf > k:
                dictionary[s[left]] -= 1
                left += 1
            result = max(result, i - left + 1)
        return result
            