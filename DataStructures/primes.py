import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# O(sqrt(n)) time complexity
def is_prime_faster(n):
    if n < 2:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# O(n/log(n)) time complexity
def is_prime_fastest(n, primes_under_sqrt_n):
    if n < 2:
        return False
    for i in primes_under_sqrt_n:
        if n % i == 0:
            return False
    return True

def euler_phi(n, primes_under_sqrt_n):
    result = n
    for p in primes_under_sqrt_n:
        if n % p == 0:
            result -= result // p
            # equivalent to result *= (1 - 1 // p)
    # add in last factor
    if n > 1:
        result -= result // n
    return int(result)

def sieve_of_eratosthenes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes

def prime_factorization(n, primes_under_sqrt_n):
    prime_factors = []
    for p in primes_under_sqrt_n:
        while n % p == 0:
            prime_factors.append(p)
            n //= p
        if n == 1:
            break
    if n > 1:
        prime_factors.append(n)
    return prime_factors

print(is_prime_faster(int(1e9 + 7)))
primes = sieve_of_eratosthenes(1_000_000)
print("Primes under 1_000_000:", len(primes))
print(prime_factorization(142_391_208_960, primes))

primes = sieve_of_eratosthenes(1_000)
print("Primes under 1_000:", len(primes))
print(euler_phi(1000, primes))

print(f"{100:b}") # bin: 1100100
print(f"{100:x}") # hex: 64
print(f"{100:o}") # oct: 144