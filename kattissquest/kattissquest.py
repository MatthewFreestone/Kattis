# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/kattissquest
from collections import namedtuple
from functools import total_ordering

@total_ordering
class Node:
    def __init__(self, E, G, left=None, right=None):
        self.E = E
        self.G = G
        self.left = left
        self.right = right
    def __eq__(self, other):
        return self.E == other.E and self.G == other.G
    def __lt__(self, other):
        if self.E == other.E:
            return self.G < other.G
        return self.E < other.E

class BST:
    def __init__(self):
        self.root = None
        self.bad_node = Node(-1, -1)
    def insert(self, E, G):
        if self.root is None:
            self.root = Node(E, G)
        else:
            self.rec_insert(self.root, E, G)
    def rec_insert(self, node, E, G):
        # we put duplicates on the right
        if node.E > E:
            if node.left is None:
                node.left = Node(E, G)
            else:
                self.rec_insert(node.left, E, G)
        else:
            if node.right is None:
                node.right = Node(E, G)
            else:
                self.rec_insert(node.right, E, G)
    def query(self, X):
        return self.rec_query(self.root, X)
    def rec_query(self, node, X):
        # we're trying to find the node that has the largest E value <= X
        if node is None:
            return self.bad_node
        if node.E > X:
            return self.rec_query(node.left, X)
        else:
            # using max will go with E value, then tiebreak with G value
            return max(node, self.rec_query(node.right, X))
    def remove(self, node):
        self.root = self.rec_remove(self.root, node)
    def rec_remove(self, node, target):
        if node is None:
            return None
        if node == target:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # find the largest node in the left subtree
                # this will be the new root of the subtree
                # then remove the old root
                largest = self.rec_find_largest(node.left)
                node.left = self.rec_remove(node.left, largest)
                node.E = largest.E
                node.G = largest.G
                return node
        elif node.E > target.E:
            node.left = self.rec_remove(node.left, target)
        else:
            node.right = self.rec_remove(node.right, target)
        return node
    
def main():
    n = int(input())
    bst = BST()
    for _ in range(n):
        cmd, *args = input().split()
        if cmd == 'add':
            e, g = map(int, args)
            bst.insert(e, g)
        else:
            x = int(args[0])
            gold_earned = 0
            while (res := bst.query(x)) != bst.bad_node:
                # we can use the node, so subtract G and remove it
                x -= res.E
                gold_earned += res.G
                bst.remove(res)
            print(gold_earned)

if __name__ == "__main__":
    main()
