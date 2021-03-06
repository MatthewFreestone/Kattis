from itertools import combinations

def triangular(tri,validSets): #use for size 3
	ma = max(tri)
	if (sum(tri) - ma) > ma:
		validSets[3].add(tri)
		return True
	return False



n = int(input())
sides = []
validSets = list([set([0]) for i in range(n+1)])
for _ in range(n):
	sides.append(int(input()))

for s in combinations(sides, 3):
	triangular(s, validSets)

for r in range(4, n+1):
	#print(r)
	for s in combinations(sides, r):
		#print(s)
		this_set = True
		for subset in combinations(s, r-1):
			if subset not in validSets[r-1]:
				this_set = False
				break
		if this_set:
			validSets[r].add(tuple(s))


#print(validSets)
flat_validSets = [item for sublist in validSets for item in sublist]

#print(set(flat_validSets))
print(len(set(flat_validSets))-1)

