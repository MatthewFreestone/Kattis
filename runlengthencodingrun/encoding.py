a, string = input().split()
if a == 'E':
    count = 1
    out = []
    last_char = string[-1]
    for i, v in enumerate(string[:-1]):
        nextStr = string[i+1]
        if v == nextStr:
            count += 1
        else:
            out.append(v)
            out.append(str(count))
            count = 1
    out.append(last_char)
    out.append(str(count))
    print("".join(out))
else:
    out = []
    for i in range(0, len(string), 2):
        v, count = string[i], string[i+1]
        out.extend([v]*int(count))
    print("".join(out))
    