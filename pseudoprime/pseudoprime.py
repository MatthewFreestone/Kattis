# Rating: ~ 3.6 / 10
# Link: https://open.kattis.com/problems/pseudoprime
from sys import stdin
import math

def main():
  while True:
    p, a = map(int, stdin.readline().split())
    if p == a == 0:
      break
    # if p is prime, it cannot be a pseudoprime
    for i in range(2, int(math.sqrt(p)) + 1):
      if p % i == 0:
        # print("possible, p isnt prime", end="\t")
        if pow(a, p, p) == a:
          print("yes")
        else:
          print("no")
        break
    else:
      # p was prime
      print("no")
      
if __name__ == "__main__":
  main()
