class Solution:
    def confusingNumber(self, n: int) -> bool:
        valid = {0:0, 1:1, 6:9, 8:8, 9:6}
        number, result = n, 0
        while n:
            c = n % 10
            if c not in valid:
                return False
            result = result * 10 + valid[c]
            n //=10
        return number != result