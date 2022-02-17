def main():
    x1,y1,x2,y2 = map(int, input().split())
    print('1' if (x1-x2 >= 2 and y1-y2 >= 2) else '0')

if __name__ == "__main__":
    main()