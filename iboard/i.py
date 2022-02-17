from sys import stdin

def main():
    for inp in stdin:
        one_stuck = False
        zero_stuck = False
        for c in inp:
            if (c == '\n'):
                continue
            ones = count1s(ord(c))
            zeros = 7-ones
            if (ones % 2 == 1):
                one_stuck = not one_stuck
            if (zeros % 2 == 1):
                zero_stuck = not zero_stuck
        stuck = one_stuck or zero_stuck
        print("trapped" if stuck else "free")

def count1s(n):
    c = 0
    while n>0:
        if (n & 1):
            c+=1
        n = n >> 1
    return c
if __name__ == "__main__":
    main()