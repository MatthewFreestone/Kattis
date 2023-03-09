a = [3,2,4,5,10]
a.sort()
# equivalent
a = sorted(a)

b = [('first', 3, 'a'), ('second', 9, 'b'), ('third', 4, 'd'), ('fourth', 4, 'c'), ('fifth', 4, 'c')]
b.sort(key=lambda x: (x[1], x[2]))
print(b)