class Solution:
    def scoreOfString(self, s: str) -> int:
        i = result = 0
        j = 1
        while j < len(s):
            result += abs(ord(s[i]) - ord(s[j]))
            i+=1
            j+=1
        return result
