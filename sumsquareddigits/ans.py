def changeBase(b,n):
	ans = []
	while n>0:
		ans.append(n%b)	

		#floor division, equivalent to math.floor(n/b) 
		n = n // b 
	return ans

P = int(input())
for _ in range(P):
	# unpacks the 3 inputs into separate string variables
	K, b, n = input().split()
	# convert both b and n to integers
	b,n = int(b), int(n)

	# returns a list of strings
	newBase = changeBase(b,n)
	
	total = 0
	for digit in newBase:
		total += int(digit)**2
	print(K, total)
