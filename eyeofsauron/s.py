inp = input()
start_eye = inp.index('()')
print('correct' if len(inp) % 2 == 0 and len(inp) // 2  - 1 == start_eye  else 'fix')