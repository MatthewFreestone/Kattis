def exp(b, e):
    res = 1
    while e > 0:
        # Check 1's bit
        if e & 1:
            res *= b
        # Square base
        b *= b
        # Shift to next bit
        e >>= 1
    return res

from timeit import timeit

print(timeit('exp(25, 1023)', globals=globals(), number=10000))
print(timeit('25**1023', globals=globals(), number=10000))
print(timeit('pow(25,1023)', globals=globals(), number=10000))

pow(b,e,m)