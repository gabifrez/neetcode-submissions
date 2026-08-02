class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for character in word:
            if character not in current.children:
                current.children[character] = Node()
            current = current.children[character]
        current.word = True

    def search(self, word: str) -> bool:
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return current.word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for character in prefix:
            if character not in current.children:
                return False
            current = current.children[character]
        return True

