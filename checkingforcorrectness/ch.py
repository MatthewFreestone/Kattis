from sys import stdin

def exp(b,e,m):
    res = 1
    b %= m
    while e > 0:
        if e & 1:
            res = (res * b) % m
        b = (b*b) %m
        e >>= 1
    return res

def main():
    for line in stdin:
        a,op,b = line.split()
        a,b = map(int,(a,b))

        if op == '+':
            print((a%10000+b%10000)%10000)
        elif op == '*':
            print((a%10000 * b%10000) % 10000)
        else:
            print(exp(a,b,10000))

if __name__ == '__main__':
    main()