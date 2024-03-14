from collections import defaultdict
s = input()
d = defaultdict(int)
fn = {
    "A": ["BC", "B", "C", ""],
    "B": ["AC", "A", "C", ""],
    "C": ["AB", "A", "B", ""]
}

def add(s, t):
    if d[t] == 0:
        if t == "":
            d[s] += 1
            return True
        return False

    x = "".join(sorted(t+s))
    if len(x) == 3:
        x = ""
    d[t] -= 1
    d[x] += 1
    return True

for c in s:
    for g in fn[c]:
        if add(c, g):
            break

assert all(d[x] == 0 for x in d if x != "")
print(d[""])
