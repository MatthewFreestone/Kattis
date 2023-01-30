from collections import namedtuple
def main():

    n = int(input())
    heights = list(map(int, input().split()))
    max_height = max(heights)
    max_index = heights.index(max_height)
    best_h = -float('inf')
    stack = []

    def process(index):
        max_jump_at_index = 0
        curr_height = heights[index]
        loop_count = 1
        while stack and curr_height >= stack[-1][0]:
            print('\t', loop_count, stack)
            first_side, best_jump = stack.pop()
            max_jump_at_index = max(max_jump_at_index, curr_height - first_side + best_jump)
            loop_count += 1
        stack.append((curr_height, max_jump_at_index))
        return max(best_h, max_jump_at_index)

    stack.append((max_height, 0))
    for i in range(max_index, -1, -1):
        print(i+1, best_h)
        best_h = process(i)
    print()
    stack.append((max_height, 0))
    for i in range(max_index + 1, n):
        print(i+1, best_h)
        best_h = process(i)
    
    print(best_h)


if __name__ == "__main__":
    main()