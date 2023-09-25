a = reversed(input())
b = reversed(input())
carry = 0
res = []
v1, v2 = next(a),next(b)
while v1 and v2:
    ans = int(v1)+int(v2) + carry
    carry = ans // 10
    res.append(str(ans % 10))
    v1 = next(a, None)
    v2 = next(b, None)
while v1:
    #we still have stuff left in v1
    ans = int(v1) + carry
    carry = ans // 10
    res.append(str(ans % 10))
    v1 = next(a, None)
while v2:
    #we still have stuff left in v2
    ans = int(v2) + carry
    carry = ans // 10
    res.append(str(ans % 10))
    v2 = next(b, None)
if carry:
    res.append(str(carry))
print(''.join(reversed(res)))