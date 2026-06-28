class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        current_color = image[sr][sc]

        def dfs(image, row, column, color, current_color, visited):
            if row < 0 or column < 0 or row == len(image) or column == len(image[0]) or image[row][column] != current_color or (row, column) in visited:
                return image
            if image[row][column] == current_color:
                image[row][column] = color
            visited.append((row, column))
            dfs(image, row - 1, column, color, current_color, visited)
            dfs(image, row, column - 1, color, current_color, visited)   
            dfs(image, row, column + 1, color, current_color, visited)   
            dfs(image, row + 1, column, color, current_color, visited)   
            return image    
        
        return dfs(image, sr, sc, color, current_color, [])

        