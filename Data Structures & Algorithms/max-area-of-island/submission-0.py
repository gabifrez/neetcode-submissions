class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        max_area = 0

        def dfs(row, column):
            area = 0
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] == 0:
                return 0
            if grid[row][column] == 1:
                grid[row][column] = 0
                area = 1
            for (i, j) in directions:
                area += dfs(row + i, column + j)
            
            return area;




        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(dfs(i,j), max_area)
        return max_area
        