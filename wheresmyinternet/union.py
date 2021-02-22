def union(parents, x, y):
 	parentX = find(parents, x)
 	parentY = find(parents, y)
 	parents[parentY] = parentX
def find(parents, child):
 	if parents[child] == child:
 		return child
 	parents[child] = find(parents, parents[child])
 	return parents[child]

n,m = [int(x) for x in input().split(' ')]
parents = dict()
for i in range(n):
	parents[i+1] = i+1
for _ in range(m):
	x,y = [int(t) for t in input().split(' ')]
	union(parents, x, y)
none = True
for i in range(n):
	if find(parents, i+1) != find(parents, 1):
		none = False
		print(i+1)

if (none):
	print("Connected")