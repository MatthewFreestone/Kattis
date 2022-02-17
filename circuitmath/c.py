def main():
	input() #throw away first value
	truths = list(map(lambda x: x == "T", input().split()))
	operations = input().split()
	ins = []
	for c in operations:
		if c == "+":
			in1,in2 = ins.pop(), ins.pop()
			ins.append(in1 or in2)
		elif c == "-":
			in1 = ins.pop()
			ins.append(not in1)
		elif c == "*":
			in1,in2 = ins.pop(), ins.pop()
			ins.append(in1 and in2)
		else:
			index = ord(c) - ord('A')
			ins.append(truths[index])
	print("T" if ins.pop() else "F")

if __name__ == '__main__':
	main()

