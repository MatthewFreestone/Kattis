from collections import defaultdict
from heapq import heappush, heappop
while True:
    n,m = map(int,input().split())
    if n == 0:
        break
    edges = defaultdict(set)
    for _ in range(m):
        i, j, w = input().split()
        i,j = int(i), int(j)
        w = float(w)
        edges[i].add((j,w))
        edges[j].add((i,w))

    pq = [(-1, 0)]
    dists = {}
    while pq:
        dist, curr = heappop(pq)
        if curr in dists:
            continue
        dists[curr] = -dist
        if curr == n-1:
            print(f"{-dist:.4f}")
            break
        for x,w in edges[curr]:
            if x not in dists:
                heappush(pq, (w*dist,x))

