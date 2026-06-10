class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1, word2 = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in word1:
                word1[s[i]] = 1
            else:
                word1[s[i]] += 1
            # ----------------------------------------------- count each character from both words
            if t[i] not in word2:
                word2[t[i]] = 1
            else:
                word2[t[i]] += 1
        # now we verify if the words are anagram
        for char in word1:
            if char not in word2:
                return False
            elif word2[char] != word1[char]:
                return False
        return True
