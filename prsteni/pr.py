from fractions import Fraction

n = int(input())
rings = list(map(int,input().split()))
outs = [Fraction(1,1)]*n
for i in range(n-1):
	outs[i] = (Fraction(rings[i]/rings[i+1])).limit_denominator(10000000)*outs[i-1]
	
for f in range(len(outs)-1):
	print(f"{outs[f].numerator}/{outs[f].denominator}")