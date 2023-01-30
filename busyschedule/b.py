def main():
    while True:
        n = int(input())
        if n == 0:
            break
        items = []
        for _ in range(n):
            original = input()
            date_str, ampm = original.split()
            hour,min = map(int, date_str.split(':'))
            if ampm == 'p.m.' and hour != 12:
                hour += 12
            elif ampm == 'a.m.' and hour == 12:
                hour -= 12
            dur = hour*100+min
            items.append((dur, original))
        items.sort(key=lambda x: x[0])
        print('\n'.join((item[1] for item in items)), '\n')


if __name__ == '__main__':
    main()