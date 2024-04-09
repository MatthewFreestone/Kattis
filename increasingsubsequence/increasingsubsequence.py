# Rating: ~ 4.0 / 10
# Link: https://open.kattis.com/problems/increasingsubsequence
from bisect import bisect_left

def backtrack(lis_end, a, parents_list):
    lis = []
    while lis_end != -1:
        lis.append(a[lis_end])
        lis_end = parents_list[lis_end]
    return lis[::-1]

def main():
    while True:
        i = input()
        if i == '0':
            break
        _, *a = list(map(int, i.split()))
        best_solns = []
        current = []
        current_ids = []
        length = 0
        parents = [-1] * len(a)
        lis_end = -1
        for i, val in enumerate(a):
            pos = bisect_left(current, val)

            if pos > 0:
                parents[i] = current_ids[pos - 1]

            if pos == length:
                length += 1
                current.append(val)
                current_ids.append(i)
                lis_end = i
                # we have increased the size of the LIS
                # time to record the path to get there
                best_solns = [backtrack(lis_end, a, parents)]
                # print('best_soln', best_soln)
            else:
                current[pos] = val
                current_ids[pos] = i

            if pos == length - 1:
                # not normally important, but is here
                lis_end = i

            best_solns.append(backtrack(lis_end, a, parents))
        lex_lowest_lis = min(best_solns)
        print(length, ' '.join(map(str, lex_lowest_lis)))

if __name__ == "__main__":
  main()


