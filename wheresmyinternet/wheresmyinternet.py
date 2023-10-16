from collections import defaultdict
n,m = map(int,input().split())
edges = defaultdict(list)
for _ in range(m):
    v1, v2 = map(int,input().split())
    edges[v1].append(v2)
    edges[v2].append(v1)

visited = set()
stack = []
stack.append(1)

while stack:
    curr = stack.pop()
    visited.add(curr)

    for adj in edges[curr]:
        if adj not in visited:
            stack.append(adj)

if len(visited) == n:
    print("Connected")
else:
    diff = set(range(1,n+1)) - visited
    diff = list(sorted(diff))
    print("\n".join(str(d) for d in diff))
