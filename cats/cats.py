from sys import stdin
t = int(stdin.readline().strip())
for _ in range(t):
    m,c = map(int,stdin.readline().split())
    parents = list(range(c+1))

    edges = []
    for _ in range((c*(c-1))//2):
        i, j, dist = map(int, stdin.readline().split())
        edges.append((dist, i, j))
    edges.sort()

    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    
    def union(x,y):
        parents[find(x)] = find(y)

    cats_connected = 1
    for dist,x,y in edges:
        if find(x) == find(y): continue
        if cats_connected == c: 
            print("yes")
            break
        m -= dist + 1
        cats_connected += 1
        union(x,y)
        if m < 0:
            print("no")
            break
    else:
        print("yes")


