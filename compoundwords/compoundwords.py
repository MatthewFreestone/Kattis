# Rating: ~ 1.8 / 10
# Link: https://open.kattis.com/problems/compoundwords
from itertools import combinations
from sys import stdin
def main():
    words = []
    for line in stdin.readlines():
        words += line.strip().split()
    combos = set()
    for a, b in combinations(words, 2):
        combos.add(a + b)
        combos.add(b + a)
    for word in sorted(combos):
        print(word)

if __name__ == "__main__":
  main()
