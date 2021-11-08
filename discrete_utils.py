from math import gcd
class Fraction:
    def __init__(self,n=0,d=1):
        self.n = n
        if d == 0:
            raise ValueError("Denominator cannot be 0")
        self.d = d
        self.simplify()
    def set_n(self,n):
        self.n = n
        self.simplify()
    def set_d(self,d):
        self.d = d
        if d == 0:
            raise ValueError("Denominator cannot be 0")
        self.simplify()
    def __str__(self):
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"
    def __int__(self):
        return self.n // self.d
    def __float__(self):
        return self.n / self.d
    def __repr__(self):
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"
    def __add__(self,a):
        if type(a) is int:
            return Fraction((self.n + a * self.d),self.d)
        if type(a) is Fraction:
            lcm = lambda a,b: abs(a*b) // gcd(a, b)
            new_d = lcm(self.d, a.d)
            return Fraction(self.n * (new_d//self.d) + a.n * (new_d//a.d), new_d)
        else:
            raise ValueError("Added with a non int or frac")
    def __sub__(self,a):
        if type(a) is Fraction:
            t = Fraction(-a.n, a.d)
            return self.__add__(t)
        if type(a) is int:
            return self.__add__(a)
        else:
            raise ValueError("Subracted by a non int or frac")
    def __mul__(self, a):
        if type(a) is int:
            return Fraction(self.n * a,self.d)
        if type(a) is Fraction:
            return Fraction(self.n*a.n, a.d*self.d)
        else:
            raise ValueError("Multiplied with a non int or frac")
    def __truediv__(self,a):
        if type(a) is int:
            return Fraction(self.n, a*self.d)
        if type(a) is Fraction:
            return Fraction(self.n*a.d, a.n*self.d)
        else:
            raise ValueError("Divided by a non int or frac")
    def __pow__(self, a):
        return Fraction(self.n**a, self.d**a)
    def __lt__(self,a):
        return float(self) < float(a)
            
    def simplify(self):
        g = gcd(self.n,self.d)
        self.n //= g
        self.d //= g
    
def fact(n):
    if n<1:
        return 1
    return n*fact(n-1)
C = lambda n,k: fact(n)//(fact(n-k)*fact(k))
P = lambda n,k: fact(n)//fact(n-k)