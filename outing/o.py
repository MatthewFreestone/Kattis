def union(s,a,b):
    if not a == b:
        r_a  = find(s,a)
        r_b = find(s,b)
        if not r_a == r_b:
            if s[r_a] <= s[r_b]:
                s[r_a] += s[r_b]
                s[r_b] = r_a
            else:
                s[r_b] += s[r_a]
                s[r_a] =  r_b
def find(s,a):
    if s[a] < 0:
        return a
    else:
        return find(s, s[a])
    
n,k = map(int,input().split())
l = [int(c)-1 for c in input().split()]
s = [-1 if not l[i] == i else -10001 for i in range(n)]
print(l)
print(s)
for i in range(len(l)):
    union(s,i,l[i])
    print(s)
groups = []
free = 0
for x in s:
    if x <= -10000:
        free -= x + 10000
    elif x < 0:
        groups.append(-x)
print(s, groups, free)