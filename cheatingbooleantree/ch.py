def main():
    t = int(input())
    for i in range(t):
        m,v = map(int, input().split())

        tree = []

        for _ in range((m-1) // 2):
            tree.append(tuple(map(int,input().split())))

        for _ in range((m+1) //2):
            tree.append(int(input()))

        vals = [0 for _ in range(m)]
        get_value(tree, vals, 0)

        min_ = get_min_changes(tree, vals, 0, v)

        if min_ == float('inf'):
            print()

        print(vals)

def get_min_changes(tree, vals, v, target_value):
    if target_value == tree[v]:
        return 0
    
    if len(tree[v]) == 1:
        return float('inf')

    operator, can_change = tree[v]
    min_no_change = -1
    min_change = -1


    if can_change:
        if operator == 1:
            if target_value == 1:
                min_no_change = get_min_changes(tree, vals, 2*v + 1, 1) + get_min_changes(tree, vals, 2*v + 2, 1)
            else:
                min_no_change = min(get_min_changes(tree, vals, 2*v + 1, 0), get_min_changes(tree, vals, 2*v + 2, 0))
        else:
            if target_value == 0:
                min_no_change = get_min_changes(tree, vals, 2*v + 1, 0) + get_min_changes(tree, vals, 2*v + 2, 0)
            else:
                min_no_change = min(get_min_changes(tree, vals, 2*v + 1, 1), get_min_changes(tree, vals, 2*v + 2, 1))
    else:
        if operator == 0: #?
            if target_value == 1:
                min_change = get_min_changes(tree, vals, 2*v + 1, 1) + get_min_changes(tree, vals, 2*v + 2, 1)
            else:
                min_change = min(get_min_changes(tree, vals, 2*v + 1, 0), get_min_changes(tree, vals, 2*v + 2, 0))
        else:
            if target_value == 0:
                min_change = get_min_changes(tree, vals, 2*v + 1, 0) + get_min_changes(tree, vals, 2*v + 2, 0)
            else:
                min_change = min(get_min_changes(tree, vals, 2*v + 1, 1), get_min_changes(tree, vals, 2*v + 2, 1))

    if min_no_change < min_change + 1:
        return min_no_change
    return min_change

def get_value(tree,vals,v):
    if len(tree[v]) == 1:
        vals[v] = tree[v][0]
        return tree[v][0]

    operator, _ = tree[v]
    if operator == 1:
        vals[v] = (get_value(tree,vals,2*v+1) & get_value(tree, vals, 2*v))
    else:
        vals[v] = (get_value(tree,vals,2*v+1) | get_value(tree, vals, 2*v))

    return vals[v]

if __name__ == "__main__":
    main()