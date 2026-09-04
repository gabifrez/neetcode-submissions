class Node:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #creating the data structure for words character by character
        trie = Node()
        for word in words:
            current = trie
            for c in word:
                if c not in current.children:
                    current.children[c] = Node()
                current = current.children[c]
            current.word = word

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        result = set()
        def dfs(row, col, visited, trie):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] not in trie.children or [row, col] in visited:
                return

            visited.append([row, col])
            trie = trie.children[board[row][col]]
    
            if trie.word:
                result.add(trie.word)
            for direction in directions:
                dfs(row + direction[0], col + direction[1], visited, trie)
            visited.pop()

        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, [], trie)
        return list(result)

        
        