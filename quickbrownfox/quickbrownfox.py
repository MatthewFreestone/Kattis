# Rating: ~ 1.8 / 10
# Link: https://open.kattis.com/problems/quickbrownfox
from string import ascii_lowercase
def main():
    n = int(input())
    for _ in range(n):
        s = set(input())
        s = {i.lower() for i in s if i.isalpha()}
        rem = set(ascii_lowercase) - s
        if len(rem) == 0:
            print("pangram")
        else:
            print(f"missing {''.join(sorted(rem))}")
if __name__ == "__main__":
  main()
