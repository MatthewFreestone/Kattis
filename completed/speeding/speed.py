import math
n = int(input())
speeds = []
pics = []
for _ in range(n):
	pics.append(list(map(int,input().split())))

for i in range(1, n):
	pt, pd = pics[i-1]
	t,d = pics[i]
	dt = t-pt
	dd = d-pd
	speeds.append(dd/dt)

print(math.floor(max(speeds)))