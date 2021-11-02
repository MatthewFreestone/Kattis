from heapq import heappop as pop, heappush as push
from collections import defaultdict 
def main():
    while True:
        inp = input()
        if inp == "0":
            break

        n,m = map(int,inp.split())
        graph = defaultdict(dict)
        for _ in range(m):
            a,b,d = map(int, input().split())
            graph[a][b] = d
            graph[b][a] = d
        
        distances = dijkstras(graph, 2) ##Create
        paths = 0
        q = [1]
        while q:
            curr = q.pop()
            if curr == 2:
                paths += 1
            else:
                for next in graph[curr]:
                    if distances[next] < distances[curr]:
                        q.append(next)
        print(paths)
        
def dijkstras(graph: dict[int, dict[int,int]], source: int) -> dict[int,int]:
    vis = {}
    pq = [(0,source)]
    while pq and len(vis) < len(graph):
        dist, curr = pop(pq)
        if curr in vis:
            continue
        vis[curr] = dist
        for next in graph[curr]:
            w = graph[curr][next]

if __name__ == "__main__":
    main()