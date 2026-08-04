class Solution:
    def confusingNumber(self, n: int) -> bool:
        if n in [6,9]:
            return True
        numbers = [0] * 10
        invalid = [2,3,4,5,7]
        length, mmax = 0, 0
        while n:
            c = n % 10
            if c in invalid:
                return False
            numbers[c] += 1
            mmax = max(mmax, numbers[c])
            length +=1
            n //=10
        if mmax == length:
            return False
        return True