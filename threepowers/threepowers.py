# Rating: ~ 2.4 / 10
# Link: https://open.kattis.com/problems/threepowers
import sys
def main():
    for l in sys.stdin:
        res = []
        l = int(l) - 1
        if l == -1:
            return
        i = 0
        while l > 0:
            if l & 1:
                res.append(3**i)
            i += 1
            l >>= 1
        print('{',', '.join(map(str,res)), '}')
        

if __name__ == "__main__":
  main()
