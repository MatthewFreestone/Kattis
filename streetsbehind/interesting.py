import math
import decimal
import sys

n, a, b = 134, 67, 96
y1 = math.floor(((b-a) / a) * n)
y2 = math.floor(n*(b-a) / a)
y3 = (b-a) * n // a

print(f"{y1=}, {y2=}, {y3=}")

c = (b-a) / a
print(type(c), sys.getsizeof(c))
print(c)

decimal.getcontext().prec = 6
n,a,b = map(decimal.Decimal, [n,a,b])
c = (b-a) / a
print(type(c), sys.getsizeof(c))
y4 = ((b-a) / a) * n
print(f"{y4=}")
