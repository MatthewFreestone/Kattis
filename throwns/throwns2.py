class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

n,k = input().split()
n = int(n)
k = int(k)
instructions = input().split()

head = Node(0)
curr = head
for i in range(1, n):
    new_node = Node(i)
    curr.next = new_node
    new_node.prev = curr
    curr = new_node
curr.next = head
head.prev = curr

curr = head
moves = []
for i in range(len(instructions)):
    # print(instructions[i], curr.value)
    instruction = instructions[i]
    if instruction == 'undo':
        continue
    if instructions[i-1] == 'undo':
        instruction = int(instruction)
        for _ in range(instruction):
            to_undo = moves.pop()

            if to_undo > 0:
                for _ in range(to_undo):
                    curr = curr.prev
            elif to_undo < 0:
                for _ in range(to_undo):
                    curr = curr.next

        pass
    else:
        instruction = int(instruction)
        moves.append(instruction)
        if instruction > 0:
            for _ in range(instruction):
                curr = curr.next
        elif instruction < 0:
            for _ in range(instruction):
                curr = curr.prev
print(curr.value)