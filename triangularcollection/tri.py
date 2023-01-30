from itertools import combinations

def triangular(tri,validSets): #use for size 3
	ma = max(tri)
	if (sum(tri) - ma) > ma:
		validSets[3].add(tri)
		return True
	return False


def triOver3(subset,validSets):
	out = []
	size = len(subset)
	if (size == 3):
		if triangular(subset,validSets):
			return True
		else:
			return False
		
	this_set = [] #boolean
	for s in combinations(subset, size-1):
		this_set.append(triOver3(s, validSets))
		#print(this_set)
	if (all(this_set)):
		validSets[size].add(tuple(subset))
		return True


n = int(input())
sides = []
validSets = list([set([0]) for i in range(n+1)])
for _ in range(n):
	sides.append(int(input()))

triOver3(sides,validSets)

print(validSets)
flat_validSets = [item for sublist in validSets for item in sublist]

print(set(flat_validSets))
print(len(set(flat_validSets))-1)

