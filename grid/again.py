from collections import deque

n, m = map(int,input().split())

grid = [[int(c) for c in input()] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

q = deque([(0,0,0)])
while q:
    x = q.popleft()
    if (x[0], x[1]) == (n-1, m-1):
        print(x[2])
        quit()
    new = [(x[0], x[1] - grid[x[0]][x[1]], x[2]+ 1),
           (x[0], x[1] + grid[x[0]][x[1]], x[2]+ 1),
           (x[0] - grid[x[0]][x[1]], x[1], x[2]+ 1),
           (x[0] + grid[x[0]][x[1]] , x[1], x[2]+ 1)
           ]
    for pos in new:
        if 0 <= pos[0] < n and 0 <= pos[1] < m and visited[pos[0]][pos[1]] == 0:
            q.append(pos)
            visited[pos[0]][pos[1]] = 1
print(-1)