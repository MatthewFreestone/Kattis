def union(parents, x, y):
 	parentX = find(parents, x)
 	parentY = find(parents, y)
 	parents[parentY] = parentX
def find(parents, child):
 	if parents[child] == child:
 		return child
 	parents[child] = find(parents, parents[child])
 	return parents[child]

r,c = map(int, input().split())
parents = list(range(r*c))
flat = []
for i in range(r):
    mapLine = input()
    for num in mapLine:
        flat.append(int(num))

n = int(input())
points = [[]] * n
for i in range(n):
    coords = map(int, input().split())
    points[i]= coords

for x in range(len(flat)):
	if x % c != c-1 and flat[x] == flat[x+1]: #add to the right
		union(parents, x, x+1)
	if x % c != 0 and flat[x] == flat[x-1]: #add to the left
	    union(parents, x, x-1)
	if x - c > 0 and flat[x] == flat[x-c]: #add above
	    union(parents, x, x-c)
	if (x + c) < (r*c) and flat[x] == flat[x+c]: #add below
		union(parents, x, x+c)

for (r1,c1,r2,c2) in points:
    #print("points ", x1,y1,x2,y2)
    sIndex = (c1-1) + c*(r1-1)
    eIndex = (c2-1) + c*(r2-1)
    if (find(parents, sIndex) == find(parents,eIndex)):
    	print("decimal" if flat[sIndex] == 1 else "binary")
    else:
    	print("neither")
