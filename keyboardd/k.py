def main():
    correct = input() + '+'
    sticky = input() + '+'
    j = 0
    out = set()
    for i in range(len(correct)):
        if correct[i] != sticky[j]:
            out.add(sticky[j])
            j += 1
        j += 1
    
    print(*out, sep='')

if __name__ == "__main__":
    main()