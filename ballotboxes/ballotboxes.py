# Rating: ~ 4.1 / 10
# Link: https://open.kattis.com/problems/ballotboxes
from heapq import heappush, heappop
from sys import stdin
from math import ceil, isclose
from functools import cache

@cache
def solve(n, b, cities):
    cities = list(cities)
    b -= n
    while b:
       curr_max, curr_boxes = heappop(cities)
       if curr_max == 1:
           break
       new_max = curr_max * (curr_boxes/(curr_boxes+1))
       heappush(cities, (new_max, curr_boxes+1))
       b -= 1
    largest, _ = heappop(cities)
    largest = abs(largest)
    # likely floating-point error
    if isclose(largest, int(largest), rel_tol=1e-8):
        out = int(largest)
    else:
        out = ceil(largest)
    return out


def main():
    input = lambda: stdin.readline().strip()
    answers = []
    while True:
        n,b = map(int,input().split())
        if n == -1 == b:
            break
        cities = []
        for _ in range(n):
            p = int(input())
            heappush(cities, (-p, 1))
        out = solve(n,b,tuple(cities))
        answers.append(out)
        input()
    print(*answers, sep="\n")
if __name__ == "__main__":
  main()
