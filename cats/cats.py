# works, prim's algorithm
from sys import stdin
from heapq import heappop, heappush
    
def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        m,c = map(int,stdin.readline().split())
        edges = [[] for _ in range(c)]
        for _ in range((c*(c-1))//2):
            i, j, dist = map(int, stdin.readline().split())
            edges[i].append((dist,j))
            edges[j].append((dist,i))
            
        cats_connected = 0
        visited = [False]*(c+1)
        pq = [(0,0)]
        while pq:
            dist, node = heappop(pq)
            if visited[node] == False:
                visited[node] = True
                cats_connected += 1
                m -= 1+dist

                if cats_connected == c:
                    break

                for d,n in edges[node]:
                    if visited[n] == False:
                        heappush(pq, (d,n))
        print("yes" if m >= 0 else "no")

if __name__ == '__main__':
    main()

