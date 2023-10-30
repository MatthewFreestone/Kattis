n = int(input())
intervals = []
for _ in range(n):
    l, u = map(int,input().split())
    intervals.append((l,u))

intervals.sort()

rooms = 1
cl, cu = intervals[0]
for l, u in intervals[1:]:
    if l > cu:
        rooms += 1
        cl, cu = l, u
    else:
        cl = max(cl, l)
        cu = min(cu, u)
print(rooms)



