class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.replace("?","")
        s = s.replace(".", "")
        s = s.replace(",", "")
        s = s.replace("!", "")
        s = s.replace("'", "")
        s = s.replace(":", "")
        s = s.lower()
        length = len(s)
        print(s)
        for i in range(length // 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True