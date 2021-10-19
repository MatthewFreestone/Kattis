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
        n.leaf += 1

    def hasPrefix(self,word):
        n = self.root
        word = word.lower()
        for c in word:
            l = ord(c) - ord('a')
            if n.children[l] == None:
                return None
            n = n.children[l]
        return n

    def countChildren(self, node):
        if not node:
            return 0
        t = 0
        if node.leaf != 0: #special case
            t += node.leaf
        for child in node.children:
            if child:
                t += self.countChildren(child)
            
        return t
      
    class TrieNode:
        def __init__(self, numChars):
            self.children = [None]*numChars
            self.leaf = 0


def main():
    n = int(input())
    t = Trie()

    for _ in range(n):
        w = input()
        pNode = t.hasPrefix(w)
        if pNode:
            print(t.countChildren(pNode))
        else:
            print(0)
        t.insert(w)

if __name__ == "__main__":
    main()