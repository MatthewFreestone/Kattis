def main():
    r, c = map(int,input().split(' '))
    graph = list([list(input()) for _ in range(r)])

    isValid = lambda x,y : -1 < x < r and -1 < y < c and graph[x][y] == '#'
    around = list(zip([-1,-1,-1,0,0,1,1,1], [-1,0,1,-1,1,-1,0,1]))

    def dfs(i,j, graph):
        graph[i][j] = '.'
        for dx,dy in around:
            x,y = i+dx, j+dy
            if isValid(x,y):
                dfs(x, y, graph)


    circles = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '#':
                circles += 1
                dfs(i,j, graph)

    print(circles)


if __name__ == '__main__':
    main()