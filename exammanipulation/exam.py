from itertools import permutations
def grade(student, key):
	g = 0
	for i in range(len(key)):
		if (key[i] == student[i]):
			g+=1
	return g


n, num_questions = map(int,input().split())
students_in = []
for _ in range(n):
	curr = [True if i == 'T' else False for i in input()]
	students_in.append(list(curr))
students = set(students_in)


key = [False]*num_questions
grades = list([grade(student, key) for student in students])

print(grades)