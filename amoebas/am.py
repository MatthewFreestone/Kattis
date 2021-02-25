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
		if (x!=n-1 and dish[x][y] == dish[x+1][y]):
			union(parents, y*n+x, y*n+x+1)
		if (x!=0 and dish[x][y] == dish[x-1][y]):
			union(parents, y*n+x, y*n+x-1)
		if (y!=m-1 and dish[x][y] == dish[x][y+1]):
			union(parents, y*n+x, (y+1)*n+x)
		if (y!=0 and dish[x][y] == dish[x][y-1]):
			union(parents, y*n+x, (y-1)*n+x)
		if (y!=m-1 and x!=n-1 and dish[x][y] == dish[x+1][y+1]):
			union(parents, y*n+x, (y+1)*n+x+1)
		if (x!=n-1 and y!=0 and dish[x][y] == dish[x+1][y-1]):
			union(parents, y*n+x, (y-1)*n+x+1)
		if (x!=n-1 and y!=m-1 and dish[x][y] == dish[x+1][y+1]):
			union(parents, y*n+x, (y+1)*n+x+1)
		if (x!=0 and y!=0 and dish[x][y] == dish[x-1][y-1]):
			union(parents, y*n+x, (y-1)*n+x-1)
for i in range(n*m):
	find(parents, i)
print(parents)
print(set(parents))
print(len(set(parents)))