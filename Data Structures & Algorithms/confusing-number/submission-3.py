class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid = [2,3,4,5,7]
        valid = {0:0, 1:1, 6:9, 8:8, 9:6}
        number, result = n, 0
        while n:
            c = n % 10
            if c in invalid:
                return False
            else:
                result = result * 10 + valid[c]
            n //=10
        return number != result