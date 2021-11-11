from math import gcd;
def simplify(n,d):
    g = gcd(n,d)
    if d < 0:
        n*= -1
        d*= -1
    return (n // g, d // g)
def lcm(a, b):
    return abs(a*b)//gcd(a,b)

ops = {
    '+': lambda an,ad,bn,bd: simplify(an * (lcm(ad,bd)//ad) + bn*(lcm(ad,bd)//bd),lcm(ad,bd)),
    '-': lambda an,ad,bn,bd: simplify(an * (lcm(ad,bd)//ad) - bn*(lcm(ad,bd)//bd),lcm(ad,bd)),
    '*': lambda an,ad,bn,bd: simplify(an*bn, ad*bd),
    '/': lambda an,ad,bn,bd: simplify(an*bd, bn*ad)
}

def main():
    n = int(input())
    for _ in range(n):
        an,ad,o,bn,bd = input().split()
        an,ad = simplify(int(an), int(ad))
        bn,bd = simplify(int(bn), int(bd))
        a,b = ops[o](an,ad,bn,bd)
        print(f"{a} / {b}")



if __name__ == '__main__':
    main()