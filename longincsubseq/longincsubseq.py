# Rating: ~ 4.9 / 10
# Link: https://open.kattis.com/problems/longincsubseq
from bisect import bisect_left

def main():
    while True:
        try:
          input()
          i = input()
        except EOFError:
          break
        a = list(map(int, i.split()))
        current = []
        current_ids = []
        length = 0
        parents = [-1] * len(a)
        lis_end = -1
        for i, val in enumerate(a):
            pos = bisect_left(current, val)
            if pos == length:
                length += 1
                current.append(val)
                current_ids.append(i)
                lis_end = i
            else:
                current[pos] = val
                current_ids[pos] = i

            if pos > 0:
                parents[i] = current_ids[pos - 1]
        lis = []
        while lis_end != -1:
            lis.append(lis_end)
            lis_end = parents[lis_end]
        lis.reverse()
        print(len(lis))
        print(' '.join(map(str, lis)))

if __name__ == "__main__":
  main()


