from collections import Counter
n, m = map(int,input().split())
people = {} #dict
for cur in range(m):
	msgs = cur + 1
	send = int(input())
	for person in people.keys():
		people[person] += 1;

	people[send] = 0
	total = (n-len(people)) * msgs
	for person in people.values():
		total += person

	print(total)