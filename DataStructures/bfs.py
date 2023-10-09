from collections import deque
graph = ["O|OOO",
         "O|OOO",
         "O|OOO",
         "OOO|O",
         "OOO|O"]

neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
inbounds = lambda x, y: 0 <= x < len(graph) and 0 <= y < len(graph[0])

queue = deque()
x,y = 0,0
path = [(x,y)]
start = (x, y, path)
queue.append(start)
visited = set()
visited.add((x, y))
end = (4, 4)

while queue:
    x, y, path = queue.popleft()
    if (x, y) == end:
        print("Found path")
        print(path)
        break
    for dx, dy in neighbors:
        new_x = x + dx
        new_y = y + dy
        if inbounds(new_x, new_y) and graph[new_x][new_y] == "O" and (new_x, new_y) not in visited:
            queue.append((x + dx, y + dy, path + [(x + dx, y + dy)]))
            visited.add((x + dx, y + dy))
else:
    print("No path found")