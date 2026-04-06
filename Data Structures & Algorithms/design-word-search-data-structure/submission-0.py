class TrieNode:
    def __init__(self):
        self.child = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        cur = self.root

        for i, ch in enumerate(word):
                if ch not in cur.child:
                    cur.child[ch] = TrieNode()
                cur = cur.child[ch]
        cur.endofword = True

    def search(self, word: str) -> bool:
        def dfs(root, i):
            cur = root
            for x in range(i, len(word)):

                if word[x]=='.':

                    for child in cur.child.values():
                        if dfs(child, x+1):
                            return True                            
                    return False
                else:                                    
                    if word[x] not in cur.child:                        
                        return False
                    cur = cur.child[word[x]]

            return cur.endofword
        
    
        i = 0
        return dfs(self.root , 0)
