from collections import defaultdict
from sys import stdin
# as it turns out, this problem has a lot of checks for variable types in deeply nested {} 
# it doesn't test a case for {{{{{{{{{{ shitload of variables }}}}}}}}}}, which makes the O(n) remove after each ok
# keeping seperated by scope and checking upwawrd progressively is too slow -- we have a lot of reads. Take that penalty in }}, not read
def main():
    n = int(input())
    output = []
    curr_scope = 0
    types_by_scope = [dict()]
    # name -> list[scopes]
    name_to_scopes = defaultdict(list)
    for _ in range(n):
        c = stdin.readline().strip()
        if c[0] == '{':
            curr_scope += 1 
            types_by_scope.append(dict())
        elif c[0] == '}':
            for k in types_by_scope[-1].keys():
                if name_to_scopes[k][-1] == curr_scope:
                    name_to_scopes[k].pop()
            types_by_scope.pop()
            curr_scope -= 1 
        elif c[0] == 'T':
            _, name = c.split()
            res = "UNDECLARED"
            if name_to_scopes[name]:
                highest_scope = name_to_scopes[name][-1]
                res = types_by_scope[highest_scope][name]
            output.append(res)
        else:
            _, name, typ = c.split()
            if name in types_by_scope[curr_scope]:
                if output:
                    print('\n'.join(output))
                print('MULTIPLE DECLARATION')
                return
            types_by_scope[curr_scope][name] = typ
            name_to_scopes[name].append(curr_scope)
    print('\n'.join(output))

if __name__ == "__main__":
    main()