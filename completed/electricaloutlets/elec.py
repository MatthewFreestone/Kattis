n = int(input())
for _ in range(n):
	total = 0
	inp = input().split(' ')
	for i in inp:
		total += int(i) - 2;
	total += 3
	print(total)
