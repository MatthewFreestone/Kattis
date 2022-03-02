def main():
    t = int(input())
    for case in range(1,t+1):
        print(f"Case #{case}")
        _, *original = map(int,input().split())
        nums = sorted(original)
        for i in range(len(nums)):
            if (i == 0):
                continue
            nums[i] += nums[i-1]
        print(nums)

if __name__ == "__main__":
    main()