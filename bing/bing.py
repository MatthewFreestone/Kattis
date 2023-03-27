from sys import stdin

input()

# at each node -> [letter, # of words below it]
trie = dict()
output = []

for line in stdin:
    word = line.strip()
    curr_node = trie
    curr_below = 0
    for char in word:
        if char in curr_node:
            curr_below = curr_node[char][1]
            curr_node[char][1] += 1
            curr_node = curr_node[char][0]
        else:
            curr_node[char] = [dict(), 1]
            curr_node = curr_node[char][0]
            curr_below = 0
    output.append(curr_below)
print(*output, sep="\n")