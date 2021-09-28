from collections import deque

r,c = map(int, input().split())
grid = [input() for _ in range(r)]
y, x = map(int,input().split())

visited = [[False] * r]*c
de = deque()

de.append((y-1,x-1,1))

around = [(1,0),(-1,0),(0,1),(0,-1)]

while len(de) > 0:
	i,j,dist = de.popleft()

	# on an edge
	if (i == 0 or i == r-1) or (j == 0 or j == c-1):
		print(dist)
		break

	for dy,dx in around:
		i_, j_ = dy+i,dx+j
		#print(y_)

		if i_ < 0 or i_ >= r or j_ < 0 or x >= c:
			continue

		if visited[i_][j_]:
			continue  
		
		visited[i_][j_] = True

		if grid[i_][j_] == 'D':
			de.appendleft(i_,j_,dist)
		elif grid[i_][j_] == 'c':
			de.append(i_,j_,dist+1)



