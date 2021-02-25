def union(parents, x, y):
 	parentX = find(parents, x)
 	parentY = find(parents, y)
 	parents[parentY] = parentX
def find(parents, child):
 	if parents[child] == child:
 		return child
 	parents[child] = find(parents, parents[child])
 	return parents[child]

m,n = [int(x) for x in input().split(' ')]
dish = [[' '*n]]*m
parents = list(range(m*n))
for y in range(m):
	dish[y] = [c for c in input()]
for y in range(m):
	for x in range(n):
		if (dish[y][x] == '#'):
			if (x!=n-1 and dish[y][x] == dish[y][x+1]):
				union(parents, y*n+x, y*n+x+1)
			if (x!=0 and dish[y][x] == dish[y][x-1]):
				union(parents, y*n+x, y*n+x-1)
			if (y!=m-1 and dish[y][x] == dish[y+1][x]):
				union(parents, y*n+x, (y+1)*n+x)
			if (y!=0 and dish[y][x] == dish[y-1][x]):
				union(parents, y*n+x, (y-1)*n+x)
			if (y!=m-1 and x!=n-1 and dish[y][x] == dish[y+1][x+1]):
				union(parents, y*n+x, (y+1)*n+x+1)
			if (x!=n-1 and y!=0 and dish[y][x] == dish[y-1][x+1]):
				union(parents, y*n+x, (y-1)*n+x+1)
			if (x!=n-1 and y!=m-1 and dish[y][x] == dish[y+1][x+1]):
				union(parents, y*n+x, (y+1)*n+x+1)
			if (x!=0 and y!=0 and dish[y][x] == dish[y-1][x-1]):
				union(parents, y*n+x, (y-1)*n+x-1)
		else:
			parents[y*n+x] = -1; #for periods
for i in range(n*m):
	find(parents, i)
print(len(set(parents))-1)