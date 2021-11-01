from collections import deque
import math

def main():
    n,m = map(int,input().split(' '))
    grid = [input() for _ in range(n)]
    isValid = lambda x,y : -1 < x < n and -1 < y < m

    def getNeighbors(i,j):
        neighbors = []
        grid_val = int(grid[i][j])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        for dx,dy in dirs:
            x, y = i + dx*grid_val, j + dy*grid_val
            if isValid(x,y):
                neighbors.append((x,y))
        return neighbors
 
    ##bfs
    visited = [(0,0)]
    queue = deque()
    queue.append((0,0,0)) #start at top-left of grid (x,y,length)
    while queue:
        c_x, c_y, c_l = queue.pop()
        if (c_x, c_y) == (n-1,m-1):
            # print("Success!")
            print(c_l)
            return
        neighbors = getNeighbors(c_x, c_y)
        for x,y in neighbors:
            if (x,y) not in visited:
                visited.append((x,y))
                queue.append((x,y, c_l+1))

    print(-1)

if __name__ == '__main__':
    main()