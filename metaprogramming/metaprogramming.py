import sys

var = dict()

for line in sys.stdin.readlines():
    p = line.split()
    if p[0] == 'define':
        var[p[2]] = int(p[1])
    else:
        if p[1] not in var or p[3] not in var:
            print('undefined')
            continue
        first = var[p[1]]
        second = var[p[3]]
        op = p[2]
        if op == '=':
            print('true' if first == second else 'false')
        elif op == '>':
            print('true' if first > second else 'false')
        elif op == '<':
            print('true' if first < second else 'false')
