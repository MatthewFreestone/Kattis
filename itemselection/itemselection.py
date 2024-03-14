import math
n,m,s,p,q = map(int,input().split())

preselected = set()
for _ in range(p):
    preselected.add(int(input()))

desired = set()
for _ in range(q):
    desired.add(int(input()))


clicks_per_page = []
for item_num in range(1, n+1, m):
    interval_length = min(m, n+1-item_num)
    selected = [1 if i in preselected else 0 for i in range(item_num, item_num+interval_length)]
    all_selected = [1] * interval_length
    none_selected = [0] * interval_length
    goal = [1 if i in desired else 0 for i in range(item_num, item_num+interval_length)]
    def difference(x,y):
        return sum([abs(i-j) for i, j in zip(x,y)])
    
    s_diff = difference(goal, selected)
    a_diff = difference(goal, all_selected) + 1
    n_diff = difference(goal, none_selected) + 1

    needed = min(s_diff, a_diff, n_diff)
    clicks_per_page.append(needed)
    # print(s_diff, a_diff, n_diff)

clicks = sum(clicks_per_page)

if clicks == 0:
    print('0')
    exit()

start = 1
end = math.ceil(n/m)

for c in clicks_per_page:
    if c == 0:
        start += 1
    else:
        break

for c in reversed(clicks_per_page):
    if c == 0:
        end -= 1
    else:
        break

if not (start <= s <= end):
    clicks += max(abs(end-s), abs(s-start)) 
else:
    clicks += min(abs(end-s), abs(s-start))
    clicks += end-start

print(clicks)
