# Rating: ~ 4.6 / 10
# Link: https://open.kattis.com/problems/boggle
from collections import namedtuple
from sys import stdin
from itertools import product
from functools import lru_cache

input = lambda: stdin.readline().strip()
Item = namedtuple('Item', 'word loc visited curr_trie')
in_bound = lambda i,j : 0 <= i < 4 and 0 <= j < 4
l2i = lambda l: ord(l) - ord('A')

def around(i,j):
    for di,dj in product([-1,0,1], repeat=2):
        ni, nj = i + di, j+dj
        if not (di == 0 and dj == 0) and in_bound(ni,nj):
            yield (ni,nj)

def score(word):
    return {3:1, 4:1, 5:2, 6:3, 7:5, 8:11}.get(len(word), 0)

def main():
    trie = [None] * 27

    wc = int(input())
    for _ in range(wc):
        word = input()
        curr = trie
        for l in word:
            idx = l2i(l)
            if curr[idx]:
                curr = curr[idx]
            else:
                curr[idx] = [None] * 27
                curr = curr[idx]
        # reached last node
        curr[-1] = True

    @lru_cache(maxsize=40)
    def solve_board(board):
        found = set()
        # do bfs to start to find words
        for i in range(4):
            for j in range(4):
                if not trie[l2i(board[i][j])]:
                    continue

                stack = []
                first = Item('', (i,j), set(), trie)
                stack.append(first)
                while stack:
                    word, loc, visited, curr_trie = stack.pop()
                    for ni,nj in around(*loc):
                        if (ni,nj) not in visited:
                            # check if this furthers a word
                            new_letter = board[ni][nj]
                            idx = l2i(new_letter)
                            if curr_trie[idx]:
                                new_word = word + new_letter
                                new_curr = curr_trie[idx]
                                if new_curr[-1]:
                                    found.add(new_word)
                                to_add = Item(new_word, (ni,nj), visited.union({(ni,nj)}), new_curr)
                                stack.append(to_add)
        return found

    input() # gross extra line
    board_ct = int(stdin.readline().strip())
    for _ in range(board_ct):
        board = tuple([input() for _ in range(4)])
        found = solve_board(board)
        longest_len = max(len(x) for x in found)
        lowest_word = min((x for x in found if len(x) == longest_len))
        print(f'{sum(map(score, found))} {lowest_word} {len(found)}')
        input() # gross extra line


    

if __name__ == "__main__":
  main()
