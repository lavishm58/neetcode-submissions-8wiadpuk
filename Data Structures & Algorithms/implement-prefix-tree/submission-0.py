class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endofword = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        cur = self.root
        for i, ch in enumerate(word):
            if not cur.children[ord(ch)-ord('a')]:
                cur.children[ord(ch)-ord('a')] = TrieNode()
            cur = cur.children[ord(ch)-ord('a')]
            if i==len(word)-1:
                cur.endofword = True


    def search(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            if not cur.children[ord(ch)-ord('a')]:
                return False
            cur = cur.children[ord(ch)-ord('a')]
            if cur.endofword:
                return True

        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for ch in prefix:
            if not cur.children[ord(ch)-ord('a')]:
                return False
            cur = cur.children[ord(ch)-ord('a')]

        return True
        
        