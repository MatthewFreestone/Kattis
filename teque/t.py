from sys import stdin
from collections import deque
class Teque:
    def __init__(self):
        self.left = deque()
        self.right = deque()
    def balance(self):
        if len(self.left) == len(self.right) or len(self.left) == len(self.right) + 1:
            return
        elif len(self.left) < len(self.right):
            self.left.append(self.right.popleft())
        elif len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
    def push_back(self,x):
        self.right.append(x)
        self.balance()
    def push_front(self,x):
        self.left.appendleft(x)
        self.balance()
    def push_middle(self,x):
        self.right.appendleft(x)
        self.balance()
    def get(self,i):
        if i > len(self.left) - 1:
            return self.right[i-len(self.left)]
        return self.left[i]
def main():
    n = int(input())
    teque = Teque()
    for line in stdin:
        cmd, x = line.split()
        if cmd == "push_back":
            teque.push_back(x)
        elif cmd == "push_front":
            teque.push_front(x)
        elif cmd == "push_middle":
            teque.push_middle(x)
        elif cmd =="get":
            print(teque.get(int(x)))

if __name__ == '__main__':
    main()