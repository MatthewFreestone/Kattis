from collections import deque

def main():
    inp = input()
    s = deque()
    for c in inp:
        if c == '<':
            s.pop()
        else:
            s.append(c)
    print(*list(s), sep='')

if __name__ == "__main__":
    main()