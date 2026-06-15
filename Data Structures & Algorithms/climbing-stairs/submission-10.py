class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        a = 1
        b = 2
        solution = 0
        for _ in range(n-2):
            solution = a+b
            a = b
            b = solution     
        return solution   