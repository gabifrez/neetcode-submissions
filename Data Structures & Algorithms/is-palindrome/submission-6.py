class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(char):
            return 'A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9'
        left = 0
        right = len(s) - 1
        while left < right:
            if not alphaNum(s[left]):
                left += 1
                continue
            if not alphaNum(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right -= 1
        return True
    