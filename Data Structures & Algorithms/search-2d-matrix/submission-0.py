class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lines, rows = len(matrix), len(matrix[0])
        left, right = 0, lines * rows - 1

        while left <= right:
            middle = (left + right) // 2

            if target > matrix[middle//rows][middle%rows]:
                left = middle + 1
            elif  target < matrix[middle//rows][middle%rows]:
                right = middle - 1
            else:
                return True

        
        return False