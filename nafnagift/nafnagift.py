from collections import deque
n1 = input()
n2 = input()

n,m = len(n1), len(n2)
queue = deque()
prevs = {}
visited = set()
queue.append((0,0,(-1,-1)))
while queue:
    pos1, pos2, prev = queue.popleft()
    #if pos1 <= n and pos2 <= m:
    prevs[(pos1,pos2)] = prev
    if pos1 == n and pos2 == m:
        break
    elif pos1 == n:
        nx, ny = pos1, pos2+1
        if (nx,ny) not in visited:
            queue.append((nx,ny,(pos1,pos2)))
            visited.add((nx,ny))
        continue
    elif pos2 == m:
        nx, ny = pos1+1, pos2
        if (nx,ny) not in visited:
            queue.append((nx,ny,(pos1,pos2)))
            visited.add((nx,ny))
        continue
    
    if n1[pos1] == n2[pos2]:
        nx, ny = pos1+1, pos2+1
        if (nx,ny) not in visited:
            queue.append((nx,ny,(pos1,pos2)))
            visited.add((nx,ny))
    else:
        nx, ny = pos1, pos2+1
        if (nx,ny) not in visited:
            queue.append((nx,ny,(pos1,pos2)))
            visited.add((nx,ny))
        nx, ny = pos1+1, pos2
        if (nx,ny) not in visited:
            queue.append((nx,ny,(pos1,pos2)))
            visited.add((nx,ny))

res = []
curr = (n, m)
while curr != (0,0):
    prev = prevs[curr]
    x1,y1 = curr
    x2,y2 = prev
    if (x1 - x2 == 0):
        res.append(n2[y2])
    else:
        res.append(n1[x2])

    curr = prev

print(*reversed(res), sep='')


