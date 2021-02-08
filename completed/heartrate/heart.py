n = int(input())
for _ in range(n):
	imp = input().split()
	b = int(imp[0])
	p = float(imp[1])
	diff = 60/p #dunno why, had to steal answer
	bpm = (60*b) / p
	print(bpm - diff, bpm, bpm + diff)