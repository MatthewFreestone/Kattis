def locate(stack, target):
	for i in range(len(stack)):
		if stack[i] == target:
			return i
	return -1 # not found

n = int(input())
for _ in range(n):
	m,r = map(int,input().split())
	stack = list([x+1 for x in reversed(range(m))])
	movies = input().split(' ')
	output = ''
	for id_num in movies:
		i = locate(stack, int(id_num))
		output += str(m-i-1) + ' '
		del stack[i]
		stack.append(int(id_num))

	print(output)
