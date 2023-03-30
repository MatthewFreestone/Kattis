from sys import stdin
from bisect import bisect_left, bisect_right
from collections import Counter

n, q = map(int, input().split())
problems = list(map(int, stdin.readline().strip().split()))
repeated_counter = Counter(problems)
data = sorted(repeated_counter.keys())
# data = sorted([[key, value] for key, value in repeated_counter.items()])
# print(data)

queries = [tuple(map(int, stdin.readline().strip().split())) for _ in range(q)]
for t, d in queries:
    # print()
    # print(data)
    # print(repeated_counter)
    if t == 1:
        idx = bisect_right(data, d)
        while idx < len(data):
            value = data[idx]
            if value > d and repeated_counter[value] > 0:
                print(value)
                repeated_counter[value] -= 1
                break
            idx += 1
        else:
            print(-1)
    else:
        idx = bisect_left(data, d)
        idx = idx - 1 if idx == len(data) else idx
        # print('idx', idx)
        while idx >= 0:
            value = data[idx]
            if value <= d and repeated_counter[value] > 0:
                print(value)
                repeated_counter[value] -= 1
                break
            idx -= 1
        else:
            print(-1)