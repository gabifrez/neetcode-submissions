class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0 
        word = False
        for i in range(len(s) -1, -1, -1):
            if s[i] == " " and word:
                return result
            if s[i] == " ":
                continue
            if s[i] != " ":
                word = True
            result += 1
        return result