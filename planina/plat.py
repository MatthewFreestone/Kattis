n = int(input()) + 1
change = 0
for i in range(n-1):
	change += 2**(i) 

print((2 + change)**2)