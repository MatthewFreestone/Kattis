# Rating: ~ 4.6 / 10
# Link: https://open.kattis.com/problems/boggle
from collections import deque, namedtuple
from sys import stdin
from itertools import product

input = lambda: stdin.readline().strip()
Item = namedtuple('Item', 'word loc visited')
in_bound = lambda i,j : 0 <= i < 4 and 0 <= j < 4
def around(i,j):
    for di,dj in product([-1,0,1], repeat=2):
        ni, nj = i + di, j+dj
        if not (di == 0 and dj == 0) and in_bound(ni,nj):
            yield (ni,nj)

def score(word):
    if len(word) < 3:
        return 0
    if len(word) < 5:
        return 1
    elif len(word) == 5:
        return 2
    elif len(word) == 6:
        return 3
    elif len(word) == 7:
        return 5
    else:
        return 11

def main():
    trie = {}

    wc = int(input())
    for _ in range(wc):
        word = stdin.readline().strip()
        curr = trie
        for l in word:
            if l in curr:
                curr = curr[l]
            else:
                curr[l] = {}
                curr = curr[l]
        # reached last node
        curr['leaf'] = True

    input() # gross extra line
    board_ct = int(stdin.readline().strip())
    for _ in range(board_ct):
        board = [input() for _ in range(4)]
        found = set()
        # do bfs to start to find words
        for i in range(4):
            for j in range(4):
                queue = deque()
                first = Item('', (i,j), set())
                queue.append(first)
                while queue:
                    word, loc, visited = queue.popleft()
                    for ni,nj in around(*loc):
                        if (ni,nj) not in visited:
                            # check if this furthers a word
                            new_word = word + board[ni][nj]
                            curr = trie
                            for l in new_word:
                                if l in curr:
                                    curr = curr[l]
                                else:
                                    break
                            else:
                                if 'leaf' in curr:
                                    found.add(new_word)
                                to_add = Item(new_word, (ni,nj), visited.union({(ni,nj)}))
                                queue.append(to_add)
        longest_len = max(len(x) for x in found)
        lowest_word = min((x for x in found if len(x) == longest_len))
        print(f'{sum(map(score, found))} {lowest_word} {len(found)}')
        input() # gross extra line

if __name__ == "__main__":
  main()
