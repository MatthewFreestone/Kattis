# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/veci
from itertools import permutations
def main():
    a = int(input())
    answer = float('inf')
    for choice in permutations(str(a)):
        c = int(''.join(choice))
        if c > a and c < answer:
            answer = c
    print(0 if answer == float('inf') else answer)

if __name__ == "__main__":
  main()
