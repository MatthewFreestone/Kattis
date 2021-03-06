def compare(s1,s2):
	different = 0 
	for i in range(len(s1)):
		if (s1[i] != s2[i]):
			different += 1
	return different


n, num_questions = map(int,input().split())
students_in = []
for _ in range(n):
	curr = [str(i) for i in input()]
	students_in.append(list(curr))

max_i = 0
max_j = 0
max_compare = -1
for i in range(len(students_in)):
	for j in range(len(students_in)):
		comp = compare(students_in[i], students_in[j])
		if (comp > max_compare):
			max_compare = comp
			max_j = j
			max_i = i

print(students_in[max_i])
print(students_in[max_j])
print(num_questions - max_compare)
#print(num_questions - int((max_compare/2)))


