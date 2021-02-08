n = int(input())
for _ in range(n):
	r,e,c = [int(n) for n in input().split()]
	if (e-c == r):
		print('does not matter')
	else:
		print('advertise' if (e-c > r) else 'do not advertise')