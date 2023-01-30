n = int(input())
dispT = 0
actT = 0
for _ in range(n):
	disp, act = map(int,input().split())
	dispT += disp * 60
	actT += act
avg = actT/dispT
print(avg if avg > 1 else "measurement error")