inp = input()
inp += "qq"
for i in range(len(inp)):
	if inp[i] == ':' or inp[i] == ';':
		if inp[i+1] == ')':
			print(i)
		elif inp[i+1] == '-':
			if inp[i+2] == ')':
				print(i)