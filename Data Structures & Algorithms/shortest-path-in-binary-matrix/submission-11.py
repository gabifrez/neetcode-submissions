class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        grid[0][0] = 1
        answer = 0
        queue = deque()
        queue.append((0, 0))
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        while len(queue):
            for k in range(len(queue)):
                row, column = queue.popleft()

                if row == len(grid) - 1 and column == len(grid[0]) - 1:
                    return answer + 1;

                for (i, j) in directions:
                    r, c = row + i, column + j
                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 1:
                        continue
                    grid[r][c] = 1
                    queue.append((r, c))

            answer += 1
        return -1
