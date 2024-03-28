from math import factorial
n = int(input())
for _ in range(n):
    i = int(input())
    result = factorial(i)
    answer = str(result)[-1]
    print(answer)