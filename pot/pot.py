n = int(input())
out = 0
for _ in range(n):
	inp = input()
	exp = int(inp[-1])
	num = int(inp[:-1]) ** int(exp)
	out += num

print(out)
