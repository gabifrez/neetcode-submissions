class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        p = {}
        counter = -1
        rows, cols = {}, {}
        for i in range(9):
            if i % 3 == 0:
                counter +=1
            rows[i] = set()
            cols[i] = set()
            p[i] = counter
        blocks = {}
        for row in range(3):
            for col in range(3):
                blocks[(row, col)] = set()
        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element == ".":
                    continue
                if element in rows[i] or element in cols[j] or element in blocks[(p[i],p[j])]:
                    return False
                rows[i].add(element)
                cols[j].add(element)
                blocks[(p[i],p[j])].add(element)
        return True