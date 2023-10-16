from pprint import pprint
m, n = map(int, input().split())

in_bounds = lambda x,y: 0 <= x < m and 0 <= y < n
neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]   

grid = []
for _ in range(m):
    line = list(input())
    grid.append(line)

visited = set()
def dfs_rec(x,y):
    def dfs_r(x,y):
        visited.add((x,y))

        # ?

        for dx, dy in neighbors:
            new_x, new_y = x+dx, y+dy
            if in_bounds(new_x, new_y):
                if grid[new_x][new_y] == "#":
                    if (new_x, new_y) not in visited:
                        dfs_r(new_x, new_y)
    dfs_r(x,y)


count = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == "#" and (i,j) not in visited:
            dfs_rec(i,j)
            count += 1
print(count)