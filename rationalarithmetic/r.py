from math import gcd
class Fraction:
    def __init__(self,n,d):
        self.n = int(n)
        self.d = int(d)
        self.simplify()
    def simplify(self):
        g = gcd(self.n,self.d)
        self.n //= g
        self.d //= g
        if self.d < 0:
            self.n *= -1
            self.d *= -1
    def __add__(self,a):
        lcm = lambda a,b : abs(a*b) // gcd(a,b)
        l = lcm(self.d,a.d)
        return Fraction(self.n*(l//self.d)+a.n*(l//a.d), l)
    def __sub__(self,a):
        n = Fraction(-a.n, a.d)
        return self.__add__(n)
    def __mul__(self, a):
        return Fraction(self.n * a.n, self.d * a.d)
    def __truediv__(self, a):
        return Fraction(self.n * a.d, self.d * a.n)
    def __str__(self):
        return f"{self.n} / {self.d}"

def main():
    n = int(input())
    for _ in range(n):
        ins = input().split()
        first = Fraction(ins[0], ins[1])
        second = Fraction(ins[3], ins[4])
        op = ins[2]
        if op == "+":
            print(first + second)
        elif op == "-":
            print(first - second)
        elif op == "*":
            print(first * second)
        elif op == "/":
            print(first / second)
    


if __name__ == "__main__":
    main()