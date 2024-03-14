def solve(n, k, a, b):
    d = b - a
    steps = 0
    while k > 0:
        inc = d * n // a
        if inc == 0:
            break

        # increasing inc guarantees at most sqrt(n) steps
        if k <= inc or d * (n + inc) // a != inc:
            steps += 1
            inc = min(k, inc)
            n += inc
            k -= inc
        else:
            # apply multiple steps at once
            # want to find maximum s such that floor(d * (n + inc * s) // a) == inc
            # d * (n + inc * s) < inc * a + a
            # d * n + d * inc * s < inc * a + a
            # d * inc * s < inc * a + a - d * n
            s = (inc * a + a - d * n - 1) // (d * inc)
            assert s >= 1
            s = min(s, (k + inc - 1) // inc)
            steps += s
            take = min(k, inc * s)
            n += take
            k -= take

    if k:
        return -1
    else:
        return steps


def main():
    t = int(input())
    for _ in range(t):
        n, k, a, b = map(int, input().split())
        print(solve(n, k, a, b))


if __name__ == "__main__":
    main()
