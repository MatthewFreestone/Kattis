graph = ["O|OOO",
         "O|OOO",
         "O|OOO",
         "OOO|O",
         "OOO|O"]

neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
inbounds = lambda x, y: 0 <= x < len(graph) and 0 <= y < len(graph[0])

start = (0, 0, [(0, 0)])
end = (4, 4)

def dfs(x, y, path):
    if (x, y) == end:
        print("Found path")
        print(path)
        return True
    for dx, dy in neighbors:
        new_x = x + dx
        new_y = y + dy
        if inbounds(new_x, new_y) and graph[new_x][new_y] == "O" and (new_x, new_y) not in path:
            if dfs(new_x, new_y, path + [(new_x, new_y)]):
                return True
    return False
print(dfs(0, 0, [(0, 0)]))