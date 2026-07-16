class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        current = [1] * n
        for i in range(m-1):
            prev = current
            for j in range(n-2,-1,-1):
                current[j] = prev[j] + current[j+1]
        return current[0]

