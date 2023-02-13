n = input()
used = {int(i) for i in n}
num_left = sorted(list({i for i in range(10) if i not in used}))
# print(num_left)

# we can't get a number of equal length
if not num_left:
    print("Impossible")
    exit()

digits = len(n)
first_digit = int(n[0])

before_first = 0
after_first = num_left[0]
# locate number above and below it
for i in num_left:
    if i > first_digit:
        after_first = i
        break
    before_first = i
# print(before_first, after_first)

# pad before with max number
before = str(before_first) + ''.join([str(num_left[-1])] * (digits-1))
# pad after with min number
after = str(after_first) + ''.join([str(num_left[0])] * (digits-1))

before, after = int(before), int(after)

before_diff = abs(int(n) - before)
after_diff = abs(int(n) - after)


if before_diff == after_diff:
    if before == after:
        # if we get identical
        print(before)
    else:
        print(before, after)
elif before_diff > after_diff:
    print(after)
else:
    print(before)

# print(before, after)
