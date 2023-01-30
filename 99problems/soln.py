def main():
    n = int(input())
    start = (n // 100) * 100
    extra = -1 if n % 100 < 49 else 99
    print(max(start+extra, 99))

if __name__ == '__main__':
    main()