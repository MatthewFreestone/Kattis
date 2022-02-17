def main():
    a,b = map(int,input().split())
    if b > a:
        p = "pieces" if b-a > 1 else "piece"
        print(f"Dr. Chaz will have {b-a} {p} of chicken left over!")
    else:
        p = "pieces" if a-b > 1 else "piece"
        print(f"Dr. Chaz needs {a-b} more {p} of chicken!")
if __name__ == "__main__":
    main()