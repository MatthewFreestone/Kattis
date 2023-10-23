# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/shortestpath1
from heapq import heappush as push, heappop as pop
from collections import defaultdict as dd
def main():
    while True:
        curr = input()
        if curr == '0 0 0 0':
            break
        n, m, q, s = map(int, curr.split())
        edges = dd(list)
        for _ in range(m):
            u, v, w = map(int,input().split())
            edges[u].append((v,w))
        queries = []
        for _ in range(q):
            queries.append(int(input()))
        queries_left = set(queries)
        # run dijkstras SSSP from node s
        distances = {}
        pq = [(0, s)]
        while pq and len(queries_left) > 0:
            dist, v = pop(pq)
            if v not in distances:
                distances[v] = dist
                if v in queries_left:
                    queries_left.remove(v)
                for x, weight in edges[v]:
                    if x not in distances:
                        push(pq, (dist + weight, x))
        for q in queries:
            if q not in distances:
                print("Impossible")
            else:
                print(distances[q])
        print()

if __name__ == "__main__":
  main()
