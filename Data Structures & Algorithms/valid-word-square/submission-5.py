class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i, word in enumerate(words):
            length = len(word)
            if length > len(words):
                return False
            for j, c in enumerate(word):
                if len(words[j]) <= i:
                    return False
                if words[j][i] != c:
                    return False
        return True
                

