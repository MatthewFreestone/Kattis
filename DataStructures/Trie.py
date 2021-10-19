class Trie:
    def __init__(self, numChars=26):
        self.root = self.TrieNode(numChars)
        self.numChars = numChars
    def insert(self,word):
        n = self.root
        word = word.lower()
        for c in word:
            l = ord(c) - ord('a')
            if n.children[l] == None:
                n.children[l] = self.TrieNode(self.numChars)
            n = n.children[l]
        n.leaf = True
    def search(self,word):
        n = self.root
        word = word.lower()
        for c in word:
            l = ord(c) - ord('a')
            if n.children[l] == None:
                return False
            n = n.children[l]
        return n.leaf
      
    class TrieNode:
        def __init__(self, numChars):
            self.children = [None]*numChars
            self.leaf = False