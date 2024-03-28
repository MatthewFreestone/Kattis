import math
while True:
    p, a = input().split()
    p = int(p)
    a = int(a)
    if p == a == 0:
        break

    for i in range(2, math.floor(math.sqrt(p)) + 1):
        if p % i == 0:
            # if (a ** p) % p == a:
            if pow(a, p, p) == a:
                print('yes')
            else:
                print('no')
            # we check for psuedoprime
            break
    else:
        print('no')