inp = list(input())
A =0 
B =0

for i in range(1, len(inp)):
	if i % 2:
		continue
	if inp[i] == 'A':
		A += int(inp[i+1]) 
	else:
		B += int(inp[i+1])

print('A' if A>B else 'B')

