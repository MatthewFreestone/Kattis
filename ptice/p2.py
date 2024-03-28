n = int(input())
answer = input()


def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element

adrian = []
adrian_iter = cycle('ABC')
for i in range(n+5):
    adrian.append(next(adrian_iter))

bruno = []
bruno_iter = cycle('BABC')
for i in range(n+5):
    bruno.append(next(bruno_iter))

goran = []
goran_iter = cycle('CCAABB')
for i in range(n+5):
    goran.append(next(goran_iter))

A, B, G = 0,0,0

for i, v in enumerate(answer):
    if v == adrian[i]:
        A += 1
    if v == bruno[i]:
        B += 1
    if v == goran[i]:
        G += 1

highest = max(A,B,G)
print(highest)

scores = [A,B,G]
names = ['Adrian', 'Bruno', 'Goran']
for i, n in enumerate(names):
    if scores[i] == highest:
        print(n)
    