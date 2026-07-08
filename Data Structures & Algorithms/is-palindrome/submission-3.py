class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in range(len(s)):
            if (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >='0' and s[i] <= '9'):
                result += s[i].lower()
     
        return result == result[::-1]