input()
string = input()

stack = []
mapping = {'(':')', '[':']', '{':'}'}
for i, v in enumerate(string):
    if v in ['(', '[', '{']:
        stack.append(v)
    elif v in [')', ']', '}']:
        if not stack or mapping[stack[-1]] != v:
            print(v, i)
            quit()
        else:
            stack.pop()
print('ok so far')