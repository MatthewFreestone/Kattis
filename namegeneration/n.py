
n = int(input())
names = []
c = 0
vowels = 'aeiou'
cons = 'bcdfghjklmnpqrstvwxyz'
for v1 in vowels:
    for c1 in cons:
        for v2 in vowels:
            for c2 in cons:
                for v3 in vowels:
                    if c >= n: 
                        print('\n'.join(names))
                        exit()
                    names.append(f"{v1}{c1}{v2}{c2}{v3}")
                    c += 1