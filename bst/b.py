
class Node:
    def __init__(self, v, left=None, right=None):
        self.v=v
        self.left = left
        self.right = right



def main():
    n = int(input())
    root = Node(int(input()))
    counter = 0
    print(counter)

    for _ in range(n-1):
        curr_value = int(input())
        depth = 0
        head = root
        while head: #not on a null node
            depth += 1
            if curr_value > head.v:
                if head.right:
                    head = head.right
                    continue
                else:
                    head.right = Node(curr_value)
                    break
            else:
                if head.left:
                    head = head.left
                    continue
                else:
                    head.left = Node(curr_value)
                    break
        counter += depth
        print(counter)



if __name__ == "__main__":
    main()