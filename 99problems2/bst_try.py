from sys import stdin
from bisect import bisect_left

n, q = map(int, input().split())
problems = sorted(list(map(int, stdin.readline().strip().split())))

queries = [tuple(map(int, input().strip().split())) for _ in range(q)]
for t, d in queries:
    if t == 1:
        idx = bisect_left(problems, d)
        print(idx)
    else:
        idx = bisect_left(problems, d)
        print(idx)
