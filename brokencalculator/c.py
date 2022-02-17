def main():
    n = int(input())
    prev = 1
    for _ in range(n):
        a,op,b = input().split()
        a,b = int(a),int(b)
        if op == "+":
            curr = a+b - prev
            prev = curr
        elif op == "-":
            curr = (a-b) * prev
            prev = curr
        elif op == "*":
            curr = (a*b) ** 2
            prev = curr
        elif op == "/":
            if a % 2 == 0:
                a //=2
            else:
                a += 1
                a //=2
            curr = a
            prev = curr
        print(prev)
if __name__ == "__main__":
    main()