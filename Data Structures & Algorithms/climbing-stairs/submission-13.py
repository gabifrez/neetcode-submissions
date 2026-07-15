class Solution:
    def climbStairs(self, n: int) -> int:

        memory = [0, 1]
        while n:
            temp = memory[0]
            memory[0] = memory[1]
            memory[1] += temp
            n-=1
        return memory[1]