from collections import deque
def main():
    n, m = map(int, input().split())
    grid = [[int(a) for a in input()] for _ in range(n)]
    around = lambda x: ((0,x),(0,-x),(x,0),(-x,0))
    in_range = lambda x: -1 < x[0] < n and -1 < x[1] < m
    queue = deque()
    queue.appendleft((0,0,0))
    visited = set() 
    while queue:
        i,j, steps = queue.pop()
        if i == n-1 and j == m-1:
            print(steps)
            return
        if (i,j) in visited:
            continue
        visited.add((i,j))
        curr = grid[i][j]
        neighbors = [(i+di, j+dj,steps+1) for di,dj in around(curr) if in_range((i+di, j+dj))] #and (i+di, j+dj) not in visited]
        for item in neighbors:
            queue.appendleft(item)
    print(-1)

if __name__ == '__main__':
    main()