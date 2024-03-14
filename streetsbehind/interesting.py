import math

n, a, b = 134, 67, 96
c = (b-a) / a
y1 = math.floor(c*n)
y2 = (b-a) * n // a

print(y1,y2)