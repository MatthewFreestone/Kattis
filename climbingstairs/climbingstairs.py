n, r, k = map(int,input().split())

# registration above office
if r > k:
    minimum = r
    remaining = n-r
    # steps must be done when we get to registration
    if remaining <= 0:
        # if they were, we can just go (floor -> registration -> floor) at a minimum
        # implied office stop somewhere in the middle
        print(2*r)
    else:
        # if not, just go up and down the right amount of stairs to get the rest
        # can't do odd number bc up and down, so add 1 to make it even
        if remaining % 2 == 1:
            remaining += 1
        print(2*r + remaining)
# office above registration
else:
    minimum = k + (k-r)
    remaining = n-minimum
    # we go to office first, then down to registration
    # steps must be done when we get to registration
    if remaining <= 0:
        # if they were, we can just go (floor -> office -> floor) at a minimum
        # implied registration stop somewhere in the middle
        print(2*k)
    else:
        # if not, just go up and down the right amount of stairs to get the rest
        # can't do odd number bc up and down, so add 1 to make it even
        if remaining % 2 == 1:
            remaining += 1
        print(2*k + remaining)

