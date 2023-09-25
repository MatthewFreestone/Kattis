from sys import stdin
from functools import lru_cache
from collections import defaultdict as dd 
from heapq import heappop, heappush

def solve(edges, m, c):
    cats_left = c
    milk_left = m
    visited = set()
    pq = [(0,0)]
    while pq:
        j, w = heappop(pq)
        if j in visited:
            continue
        else:
            visited.add(j)
            milk_left -= 1+w
            cats_left -= 1

            if milk_left < 0:
                return "no"
            if cats_left == 0:
                return "yes"

            for n,nw in edges[j]:
                if n not in visited:
                    heappush(pq, (n,nw))
    else:
        #this is bad, memory error time
        a = list(range(1_000_000_000_000))

def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        m,c = map(int,stdin.readline().split())
        edges = dd(list)
        for _ in range((c*(c-1))//2):
            i, j, dist = map(int, stdin.readline().split())
            edges[i].append((j,dist))
            edges[j].append((i,dist))
        if c > m:
            # more cats than milk, gonna be impossible.  
            print("no")
            continue
        result = solve(edges, m, c)
        print(result)
if __name__ == '__main__':
    main()
