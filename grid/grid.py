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
        visited.add((i,j))
        curr = grid[i][j]
        neighbors = [(i+di, j+dj,steps+1) for di,dj in around(curr) if in_range((i+di, j+dj)) and (i+di, j+dj) not in visited]
        for new_i,new_j,new_steps in neighbors:
            queue.appendleft((new_i, new_j, new_steps))
            visited.add((new_i, new_j))
    print(-1)

if __name__ == '__main__':
    main()
