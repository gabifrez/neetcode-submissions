class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        timer, fruits = 0, 0
        queue = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fruits += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
                    grid[i][j] = 0
        if (fruits == 0 and len(queue) != 0) or fruits == 0:
            return 0
        while len(queue):
            for iteration in range(len(queue)):
                row, column = queue.popleft()
                for (i, j) in directions:
                    r, c = row + i, column + j
                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                        continue
                    grid[r][c] = 0
                    queue.append((r, c))
                    fruits -= 1
            timer += 1
        
        if fruits == 0:
            return timer - 1
        else:
            return -1