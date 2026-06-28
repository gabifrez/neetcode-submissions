class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        current_color = image[sr][sc]
        if current_color == color:
            return image
        def dfs(image, row, column, color, current_color, visited):
            if row < 0 or column < 0 or row >= len(image) or column >= len(image[0]) or image[row][column] != current_color:
                return 
            
            image[row][column] = color
            dfs(image, row - 1, column, color, current_color, visited)
            dfs(image, row, column - 1, color, current_color, visited)   
            dfs(image, row, column + 1, color, current_color, visited)   
            dfs(image, row + 1, column, color, current_color, visited)   
              
        
        dfs(image, sr, sc, color, current_color, [])
        return image

        