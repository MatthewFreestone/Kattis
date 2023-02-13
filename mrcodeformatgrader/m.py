n, m = map(int,input().split())
errors = list(map(int,input().split()))

errors_together = []
streak_start = errors[0]
streak_end = errors[0]
for i in range(1, len(errors)):
    if errors[i] == errors[i-1] + 1:
        streak_end = errors[i]
    else:
        errors_together.append((streak_start, max(streak_end, streak_start)))
        streak_start = errors[i]
errors_together.append((streak_start, max(streak_end, streak_start)))

correct_together = []
start, end = errors_together[0]
start_n_streak = 1 if start != 1 else end+1
for error in errors_together:
    start, end = error
    if start_n_streak > end:
        continue
    correct_together.append((start_n_streak, start - 1))
    start_n_streak = end+1
if start_n_streak != n+1:
    correct_together.append((start_n_streak, n))

out_str = []
for start, end in errors_together:
    if start == end:
        out_str.append(str(start))
    else:
        out_str.append(f"{start}-{end}")
if len(out_str) == 1:
    print(f"Errors: {out_str[0]}")
else:
    print(f"Errors: {', '.join(out_str[:-1])} and {out_str[-1]}")

out_str = []
for start, end in correct_together:
    if start == end:
        out_str.append(str(start))
    else:
        out_str.append(f"{start}-{end}")
if len(out_str) == 1:
    print(f"Correct: {out_str[0]}")
else:
    print(f"Correct: {', '.join(out_str[:-1])} and {out_str[-1]}")