def main():
    m,n = map(int,input().split(' '))

    dish = []
    for i in range(m):
        dish.append(list(input()))
    # print(dish)
    def isValid(x,y):
        return -1 < x < m and -1 < y < n and dish[x][y] == '#'

    def getNeighbors(i,j):
        out=[]
        around = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1), (1,1),(1,0),(1,-1)]
        for dx,dy in around:
            x = i+dx
            y = j+dy
            if isValid(x,y):
                out.append((x,y))
        return out

    def dfs(i,j):
        dish[i][j] = '.'
        neighbors = getNeighbors(i,j)
        for x,y in neighbors:
            dfs(x,y)
    
    ameobas = 0
    for i in range(m):
        for j in range(n):
            if dish[i][j] == '#':
                ameobas += 1
                dfs(i,j)
    
    print(ameobas)


if __name__ == "__main__":
    main()