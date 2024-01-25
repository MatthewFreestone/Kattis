# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/sortofsorting

def main():
  while True:
    n = int(input())
    if n == 0:
      break
    names = [input() for _ in range(n)]
    names.sort(key=lambda x: x[:2])
    print('\n'.join(names), end='\n\n')

if __name__ == "__main__":
  main()
