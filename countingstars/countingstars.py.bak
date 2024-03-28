case_num = 1
around = ((0,1),(0,-1),(1,0),(-1,0))
while True:
    try:
        curr = input()
    except EOFError:
        exit()
    m,n = map(int, curr.split())
    graph = [list(input()) for _ in range(m)]
    in_range = lambda x,y: 0 <= x < m and 0 <= y < n
    def dfs(x,y):
        queue = []
        queue.append((x,y))
        while queue:
            x,y = queue.pop()
            graph[x][y] = "#"
            for dx, dy in around:
                c_x, c_y = x+dx, y+dy
                if in_range(c_x,c_y) and graph[c_x][c_y] == '-':
                    queue.append((c_x,c_y))
    count = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == '-':
                dfs(i,j)
                count += 1
    print(f"Case {case_num}: {count}")
    case_num += 1

