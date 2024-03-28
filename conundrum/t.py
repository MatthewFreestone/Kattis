
string = input()
total = 0

for i,v in enumerate(string):
	if i % 3 == 0 and v != 'P':
		total += 1
	if i % 3 == 1 and v != 'E':
		total += 1
	if i % 3 == 2 and v != 'R':
		total += 1
print(total)