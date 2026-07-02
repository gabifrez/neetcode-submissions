class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        positions = [[-1,0],[0,-1],[0,1],[1,0]]


        def dfs(row, column):
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] == "0":
                return
            grid[row][column] = "0"
            dfs(row - 1, column)
            dfs(row, column - 1)
            dfs(row, column + 1)
            dfs(row + 1, column)
        
        for i in range(0,len(grid)):
            for j in range(0, len(grid[0])):
                if(grid[i][j] == "1"):
                    dfs(i,j)
                    islands += 1
            
        return islands;


        