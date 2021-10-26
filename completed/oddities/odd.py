n = int(input())
for _ in range(n):
	c = int(input())
	p = f"{c} is even" if c%2==0 else f"{c} is odd"
	print(p)