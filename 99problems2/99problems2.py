from sys import stdin
from bisect import bisect_left
from collections import Counter

n, q = map(int, input().split())
problems = list(map(int, stdin.readline().strip().split()))
repeated_counter = Counter(problems)
data = sorted(repeated_counter.keys())
# data = sorted([[key, value] for key, value in repeated_counter.items()])
# print(data)

queries = [tuple(map(int, input().strip().split())) for _ in range(q)]
for t, d in queries:
    print(data)
    print(repeated_counter)
    if t == 1:
        idx = bisect_left(data, d) + 1
        while True:
            if 0 <= idx < len(data):
                value = data[idx]
                if repeated_counter[value] > 0:
                    print(value)
                    repeated_counter[value] -= 1
                    break
                else:
                    idx += 1
            else:
                print(-1)
                break
    else:
        pass
        # idx = bisect_left(problems, d)
        # print(idx)
