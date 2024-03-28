a = int(input())
a = bin(a)
a = ''.join(reversed(str(a[2:])))
print(int(a,2))
