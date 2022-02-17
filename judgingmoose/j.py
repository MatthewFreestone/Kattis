def main():
    r,l = map(int,input().split())
    if (r == 0 and l == 0):
        print("Not a moose")
    else:
        print(f"{'Odd' if (r != l) else 'Even'} {2*max(r,l)}") 

if __name__ == "__main__":
    main()