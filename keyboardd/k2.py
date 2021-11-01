from collections import Counter

def main():
    A = input()
    a_c = Counter()
    B = input()
    b_c = Counter()
    for c in A:
        a_c[c] += 1
    for c in B:
        b_c[c] += 1
    
    out = ''
    for c in a_c.keys():
        if a_c[c] != b_c[c]:
            out += c
    print(out)

def alt_method():
    A, B = input(), input()
    print(''.join(x for x in map(chr, range(32, 127)) if A.count(x) < B.count(x)))

if __name__ == "__main__":
    #main()
    alt_method()
