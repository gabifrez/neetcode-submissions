class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(row, col, visited, index):
            if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1 or [row, col] in visited or word[index] != board[row][col]:
                return False

            if index == len(word) - 1 and word[index] == board[row][col]:
                return True

            index+=1
            visited.append([row,col])

            for direction in directions:
                if dfs(row + direction[0], col + direction[1], visited, index):
                    return True
            visited.pop()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, [], 0):
                    return True
        return False