# Rating: ~ 5.1 / 10
# Link: https://open.kattis.com/problems/abcstring

def main():
    mapping = {'A':1,'B':2,'C':4}
    counts = [0,0,0,0,0,0,0]
    ans = 1
    for c in input():
        i = mapping[c]
        # check if we can complete a 2-set
        need_2 = 7 ^ i

        # see if we can creata a 2-set
        need_1x, need_1y = {need_2 & 4, need_2 & 2, need_2 & 1} - {0}

        #print(c, i, need_2, need_1x, need_1y)
        if counts[need_2]:
            counts[need_2] -= 1
        elif counts[need_1x]:
            counts[need_1x] -= 1
            counts[i ^ need_1x] += 1
        elif counts[need_1y]:
            counts[need_1y] -= 1
            counts[i ^ need_1y] += 1
        else:
            counts[i] += 1
        #print(counts)
        ans = max(ans, sum(counts))
    print(ans)

if __name__ == "__main__":
  main()
