n = int(input())
a = []
for _ in range(n):
	a.append(input())

total = 0
for i in range(n-1):
	if a[i] == a[i+1]:
		total += 1

print(total)