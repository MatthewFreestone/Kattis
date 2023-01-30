from itertools import combinations

a = []
for _ in range(9):
	a.append(int(input()))

comb = combinations(a, 7)
for i in list(comb):
	#print(i)
	if sum(i) == 100:
		for n in i:
			print(n)
		break