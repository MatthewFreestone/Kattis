# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/throwns

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

def main():
  n,_= map(int, input().split())
  commands = input().split()
  head = Node(0)
  curr = head
  for i in range(1,n):
    new = Node(i)
    new.prev = curr
    curr.next = new
    curr = new
  curr.next = head
  head.prev = curr

  prev_commands = []
  curr = head
  for i in range(len(commands)):
    if commands[i] == 'undo':
      continue
    if commands[i-1] == 'undo':
      to_reverse = int(commands[i])
      for _ in range(to_reverse):
        movement = prev_commands.pop()
        if movement > 0:
          for _ in range(movement):
            curr = curr.prev
        elif movement < 0:
          for _ in range(-movement):
            curr = curr.next
    else:
      movement = int(commands[i])
      prev_commands.append(movement)
      if movement > 0:
        for _ in range(movement):
          curr = curr.next
      elif movement < 0:
        for _ in range(-movement):
          curr = curr.prev
  print(curr.val)
if __name__ == "__main__":
  main()
