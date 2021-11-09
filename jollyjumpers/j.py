from sys import stdin

def main():
    for line in stdin:
        c = line.split()
        n = int(c[0])
        taken = [False for _ in range(1, n)]
        for i in range(1, len(c)-1):
            d = abs(int(c[1+i])-int(c[i]))
            if 0 < d < n:
                taken[d-1] = True
        print("Jolly" if all(taken) else "Not jolly")
if __name__ == "__main__":
    main()