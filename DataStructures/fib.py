def fib(n):
    if n <= 0:
        return 0
    elif n<= 2:
        return 1
    return fib(n-1) + fib(n-2)

from functools import cache

@cache
def fib_dp(n):
    if n <= 0:
        return 0
    elif n<= 2:
        return 1
    return fib_dp(n-1) + fib_dp(n-2)

def fib_bottomup(n):
    if n <= 0:
        return 0
    elif n<= 2:
        return 1
    a,b = 1,1
    for _ in range(n-2):
        a,b = b, a+b
    return b

from timeit import timeit 
print(timeit('fib(15)', globals=globals(), number=10000)) #1.048831499996595
print(timeit('fib_dp(15)', globals=globals(), number=10000)) #0.0012265000259503722
print(timeit('fib_bottomup(15)', globals=globals(), number=10000)) #0.0008223999757319689
