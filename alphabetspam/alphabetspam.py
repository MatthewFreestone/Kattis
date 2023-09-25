# Rating: ~ 1.5 / 10
# Link: https://open.kattis.com/problems/alphabetspam
from collections import Counter
def main():
    inp = input()
    white = 0
    lower = 0
    upper = 0
    symbol = 0

    for c in inp:
        if c == "_":
            white += 1
        elif c.isalpha():
            if ord(c) - ord('Z') > 0:
                lower += 1
            else:
                upper += 1
        else:
            symbol += 1
    l = len(inp)
    print(*[i/l for i in (white,lower,upper,symbol)], sep="\n")
            


if __name__ == "__main__":
  main()
