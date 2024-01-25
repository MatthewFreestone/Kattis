# Rating: ~ 1.5 / 10
# Link: https://open.kattis.com/problems/nodup
from collections import Counter

def main():
    print("yes" if max(Counter(input().split()).values()) == 1 else "no")

if __name__ == "__main__":
  main()
