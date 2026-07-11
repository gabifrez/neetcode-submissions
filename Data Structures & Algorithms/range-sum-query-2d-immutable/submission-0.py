class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (col + 1) for i in range(row + 1)]
        for i in range(len(matrix)):
            prefix = 0
            for j in range(len(matrix[0])):
                prefix += matrix[i][j]
                self.sumMatrix[i+1][j + 1] = prefix + self.sumMatrix[i][j+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.sumMatrix[row2][col2] - self.sumMatrix[row1-1][col2] - self.sumMatrix[row2][col1-1] + self.sumMatrix[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)