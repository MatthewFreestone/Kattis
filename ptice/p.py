input()
answers = input()

A = 0
B = 0
G = 0
i = 0
while len(answers) %6 != 0:
    answers += 'x'

for i in range(len(answers)- 2):
    if answers[i] == 'A':
        A += 1
    if answers[i+1] == 'B':
        A += 1
    if answers[i+2] == 'C':
        A += 1
    i += 3

i = 1
if answers[0] == 'B':
    B += 1
for i in range(len(answers)- 2):
    if answers[i] == 'A':
        B += 1
    if answers[i+1] == 'B':
        B += 1
    if answers[i+2] == 'C':
        B += 1
    i += 3

i = 0
for i in range(len(answers) - 5):
    if answers[i] == 'C':
        G+= 1
    if answers[i+1] == 'C':
        G+= 1
    if answers[i+2] == 'A':
        G+= 1
    if answers[i+3] == 'A':
        G+= 1
    if answers[i+4] == 'B':
        G+= 1
    if answers[i+5] == 'B':
        G+= 1
    i += 6

highest = max(A,B,G)
print(highest)

scores = [A,B,G]
names = ['Andrian', 'Bruno', 'Goran']
for i, n in enumerate(names):
    if scores[i] == highest:
        print(n)
    