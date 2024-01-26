from bisect import bisect_left
a,d = map(int,input().split())

ascend_distances = [0]
ascend_times = [0]
for _ in range(a):
    h,t = map(int,input().split())
    ph, pt = ascend_distances[-1], ascend_times[-1]
    ascend_distances.append(h+ph)
    ascend_times.append(t+pt)

descend_distances = [ascend_distances[-1]]
descend_times = [0]
for _ in range(d):
    h,t = map(int,input().split())
    ph, pt = descend_distances[-1], descend_times[-1]
    descend_distances.append(ph-h)
    descend_times.append(t+pt)

left = 0
right = min(ascend_times[-1], descend_times[-1])
dt = 1e9
while True:
    # middle is the time we're guessing
    # dist = m(time) + b
    middle = (left + right)/2
    # print(left, middle, right, end=": ")
    a_loc = bisect_left(ascend_times, middle)
    if ascend_times[a_loc] == middle:
        a_dist = ascend_distances[a_loc]
    else:
        time_before = ascend_times[a_loc-1]
        time_after = ascend_times[a_loc]
        dist_before = ascend_distances[a_loc-1]
        dist_after = ascend_distances[a_loc]
        # m = dx/dt
        m = (dist_after - dist_before) / (time_after - time_before)
        # b = y-mx
        b = dist_before - m*time_before
        # y=mx+b 
        a_dist = m*middle + b

    d_loc = bisect_left(descend_times, middle)
    if descend_times[d_loc] == middle:
        d_dist = descend_distances[d_loc]
    else:
        time_before = descend_times[d_loc-1]
        time_after = descend_times[d_loc]
        dist_before = descend_distances[d_loc-1]
        dist_after = descend_distances[d_loc]
        # m = dx/dt
        m = (dist_after - dist_before) / (time_after - time_before)
        # b = y-mx
        b = dist_before - m*time_before
        # y=mx+b 
        d_dist = m*middle + b
    
    # print(a_dist, d_dist)
    # an extra bit of precision is like 3-4 extra runs, so whatever
    if dt < 1e-7:
        print(middle)
        break

    if a_dist < d_dist:
        # gets there first on ascent. move higher
        dt = abs(middle-left)
        left = middle
    else:
        # gets there first on descent. move lower
        dt = abs(middle-right)
        right = middle

