import sys

for line in sys.stdin:
    print(line)

# OR

while True:
    line = sys.stdin.readline()
    if line == "":
        break
    print(line)