from collections import deque, namedtuple
Person = namedtuple('Person', 'operator, rest, then')
n = int(input())
absolutes = set()
ands = []
ors = []
unsatified = deque()

def check_curr(item: Person):
    if item.operator == "and":
        toppings_left = [topping for topping in item.rest if topping not in absolutes]
        if len(toppings_left) == 0:
            absolutes.add(item.then)
            return 1
        unsatified.append(Person("and", toppings_left, item.then))
        return 0
    elif item.operator == "or":
        for topping in item.rest:
            if topping in absolutes:
                absolutes.add(item.then)
                return 1
        unsatified.append(item)
        return 0
    else:
        # print(f"BAD: {item}")
        return 0

        

for i in range(n):
    cond, *rest = input().split()
    if cond != 'if':
        absolutes.add(cond)

    else:
        if rest[1] == "and":
            then = rest[-1]
            rest.pop()
            rest.pop()
            rest = set(rest)
            rest.remove('and')
            unsatified.append(Person('and', rest, then))
        else:
            then = rest[-1]
            rest.pop()
            rest.pop()
            rest = set(rest)
            unsatified.append(Person('or', rest, then))
unsatified.append(Person('start_token', None, None))
changed = 0
while len(unsatified) != 0:
    # print(unsatified)
    curr = unsatified.popleft()
    if curr.operator == "start_token":
        if changed == 0:
            print(len(absolutes))
            exit()
        changed = 0
        unsatified.append(Person('start_token', None, None))
        continue
    changed += check_curr(curr)

print(absolutes)