from collections import defaultdict
n, m = map(int,input().split())
n+= 1
parents = [i for i in range(n)]
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
        return parents[x]
    return x

def union(x, y):
    px = find(x)
    py = find(y)
    parents[py] = px

for _ in range(m):
    a, b = map(int,input().split())
    union(a,b)

# for i in range(n):
#     find(i)
# print(parents)
some = False
for i in range(1,n):
    if find(i) != find(1):
        print(i)
        some = True
if not some:
    print("Connected")