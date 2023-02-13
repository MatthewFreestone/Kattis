# f(n): count number of integers in range [1,n] that are not relatively prime to n
# g(n): f(n)/n
# find max value of g(k) where 2 < k < n

# heruristic: multiply primes until we're above n
# 	This will have the most possible factors
# 	Check the g(n) for each 
from fractions import Fraction
from math import gcd, prod
n = int(input())
best_k = 2
primes = [2]
for i in range(3, n):
    if gcd(i,best_k) == 1:
        best_k *= i
        primes.append(i)
    if best_k > n:
        best_k //= i
        primes.pop()
        # print(primes)
        break
# euler's phi to find # of relatively prime
non_rel_prime = best_k - prod([x-1 for x in primes])
print(Fraction(non_rel_prime, best_k))
# print(best_k)

