import math
while True:
    try:
        i = input()
    except:
        exit()
    n, length, width  = map(int,i.split())
    sprinker_right_to_left = {}
    # sprinklers = []
    for _ in range(n):
        x, r = map(int,input().split())
        if 2*r <= width:
            continue
        # draw a triangle from radius to top corner of the box it touches
        # that ray has length r, and the triangle has height w/2
        # the value we want is the distance left and right, which is the other num
        # r^2 = (w/2)^2 + des^2
        des = math.sqrt(r**2 - (width/2)**2)

        # cap the left and right at the ends of the strip.
        # we don't want a case where a huge sprinker in middle is forgotten over a two smaller on each end.
        left = 0 if (x-des) < 0 else (x-des)
        right = length if (x+des) > length else (x+des)
        if right in sprinker_right_to_left:
            sprinker_right_to_left[right] = min(sprinker_right_to_left[right], left)
        else:
            sprinker_right_to_left[right] = left

    if not sprinker_right_to_left:
        print(-1)
        continue

    sprinklers = [(l,r) for r, l in sprinker_right_to_left.items()]
    sprinklers.sort(key=lambda x: x[1], reverse=True)
    first_left, first_right = sprinklers[0]
    if first_right < length:
        print(-1)
        continue
    if first_left == 0:
        print(1)
        continue

    uncovered_left = first_left
    best_left = first_left
    num_sprinklers = 1
    for left, right in sprinklers[1:]:
        if best_left == 0:
            break
        if right < uncovered_left:
            uncovered_left = best_left
            num_sprinklers += 1
            best_left = left
            if right < uncovered_left:
                num_sprinklers = -1
                break
        best_left = min(left, best_left)

    if best_left == 0:
        num_sprinklers += 1
        print(num_sprinklers)
    else:
        print(-1)
    # print()
