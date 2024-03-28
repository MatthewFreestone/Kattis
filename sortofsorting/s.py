#https://open.kattis.com/problems/sortofsorting
while True:
    n = int(input())
    if n == 0:
        exit()
    names = []
    for _ in range(n):
        i = input()
        names.append(i)
    names.sort(key=lambda x: x[:2])
    for i in names:
        print(i)
    print()