from collections import deque
from sys import stdin
def main():
    n = int(input())
    first_half = deque()
    second_half = deque()
    def balance():
        # if odd, keep first half longer.
        # if even, keep them equal
        if len(second_half) > len(first_half):
            first_half.append(second_half.popleft())
        elif len(second_half) + 1 < len(first_half):
            second_half.appendleft(first_half.pop())
            
    output = []
    for _ in range(n):
        req, num = stdin.readline().strip().split()
        num = int(num)
        if req == "push_back":
            second_half.append(num)
            balance()
        elif req == "push_front":
            first_half.appendleft(num)
            balance()
        elif req == "push_middle":
            first_half.append(num)
            balance()
        elif req == "get":
            if num < len(first_half):
                output.append(first_half[num])
            else:
                output.append(second_half[num - len(first_half)])
    print('\n'.join((str(num) for num in output)))

if __name__ == "__main__":
    main()
