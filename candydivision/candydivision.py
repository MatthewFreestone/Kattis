# Rating: ~ 3.8 / 10
# Link: https://open.kattis.com/problems/candydivision

def main():
    n = int(input())
    options = [0]
    ans = set(options)
    for i in range(1, int(n**(1/2))):
        if n % (i+1) == 0:
            options.append(i)
            ans.add(i)
    for i in reversed(options):
        ans.add((n//(i+1))-1)
    print(*sorted(ans))

if __name__ == "__main__":
  main()
