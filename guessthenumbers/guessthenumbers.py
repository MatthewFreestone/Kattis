#PYTHON USERS UP !! 
from itertools import permutations
while True:
    l = [*map(int,input().split())]
    if l[0] == 0:
        break
    nums = l[1:-1]
    res = l[-1]
    expression = input()
    letters = [*{a for a in expression if a.isalpha()}]
    
    parse_string = []
    for c in expression:
        if c.isalpha():
            parse_string.append(f"v['{c}']")
        else:
            parse_string.append(c)
    # python eval is SLOW, but we can trick it
    # if we use the eval to create a function (as a lambda)
    # then run that expression repeatedly as if we'd defined it in code
    py_expr = eval('lambda :' + ''.join(parse_string))
    for combo in permutations(nums):
        v = {l:n for l,n in zip(letters, combo)}
        cres = py_expr()
        if cres == res:
            print("YES")
            break
    else:
        print("NO")
