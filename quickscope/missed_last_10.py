from collections import defaultdict
from sys import stdin
def main():
    n = int(input())
    output = []
    curr_scope = 0
    # scope_num:int -> dict(name:str -> type:str)
    types = defaultdict(dict)
    for _ in range(n):
        c = stdin.readline().strip()
        if c[0] == '{':
            curr_scope += 1 
            continue
        if c[0] == '}':
            types[curr_scope] = {}
            curr_scope -= 1 
            continue
        if c[0] == 'T':
            _, name = c.split()
            res = "UNDECLARED"
            for i in range(curr_scope, -1, -1):
                if name in types[i]:
                    res = types[i][name]
                    break
            output.append(res)
            # print(types[curr_scope].get(name, "UNDECLARED"))
            continue
        _, name, typ = c.split()
        if name in types[curr_scope]:
            if output:
                print('\n'.join(output))
            print('MULTIPLE DECLARATION')
            return
        types[curr_scope][name] = typ
    print('\n'.join(output))

if __name__ == "__main__":
    main()