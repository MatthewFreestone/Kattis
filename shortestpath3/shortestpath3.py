# Rating: ~ 4.7 / 10
# Link: https://open.kattis.com/problems/shortestpath3

def main():
    while True:
        n,m,q,s = map(int,input().split())
        if n == 0:
            break;
        edges = []
        for _ in range(m):
            u,v,w = map(int,input().split())
            edges.append((u,v,w))
        queries = []
        for _ in range(q):
            c = int(input())
            queries.append(c)
        distances = [1e9] * n
        distances[s] = 0
        for _ in range(1,n):
            for u,v,w in edges:
                if distances[u] != 1e9 and distances[u]+w<distances[v]:
                    distances[v] = distances[u] + w
        # check for negative cycles
        for _ in range(1,n):
            for u,v,w in edges:
                if distances[u] != 1e9 and distances[u]+w<distances[v]:
                    distances[v] = -1e9
        for q in queries:
            c = distances[q]
            if c == 1e9:
                print("Impossible")
            elif c == -1e9:
                print("-Infinity")
            else:
                print(c)
        print()

if __name__ == "__main__":
  main()
