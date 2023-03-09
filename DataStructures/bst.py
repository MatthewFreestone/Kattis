class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, element):
        n = self.root
        if n == None:
            self.root = self.Node(element)
            return
        while True:
            if element < n.element:
                if n.left == None:
                    n.left = self.Node(element)
                    return
                n = n.left
            else:
                if n.right == None:
                    n.right = self.Node(element)
                    return
                n = n.right
    def search(self, element):
        n = self.root
        while n != None:
            if element < n.element:
                n = n.left
            elif element > n.element:
                n = n.right
            else:
                return True
        return False
    def __str__(self):
        return self.strHelper(self.root)
    def strHelper(self, n):
        ''' Inorder traversal '''
        if n == None:
            return ""
        return self.strHelper(n.left) + str(n.element) + " " + self.strHelper(n.right)

    class Node:
        def __init__(self, element):
            self.element = element
            self.left = None
            self.right = None
    
a = BinarySearchTree()
a.insert(7)
a.insert(5)
a.insert(9)

print(a)
print(a.search(5))
print(a.search(6))