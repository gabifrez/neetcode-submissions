class Solution:
    def uniquePathsWithObstacles(self, Grid: List[List[int]]) -> int:
        rows, column = len(Grid), len(Grid[0])
        current = [0] * (column + 1)
        current[-2] = 1
        for i in range(rows-1,-1,-1):
            for j in range(column - 1, -1, -1):
                if Grid[i][j] == 1:
                    current[j] = 0
                else:
                    current[j] = current[j] + current[j+1]
        return current[0]
                

