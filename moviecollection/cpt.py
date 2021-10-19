from sys import stdin
def main():
    inp = lambda : stdin.readline()
    t = int(inp())

    for _ in range(t):
        m,r = map(int,inp().split())
        movies = [*map(int,inp().split())]

        tree = [0 for _ in range(m+r+1)]
        movie_pos = {}

        for i in range(1,m+1):
            movie_pos[i] = m-i+1
            update(tree, i, 1)

        outs = []
        time = m+1
        for movie in movies:
            idx = movie_pos[movie]
            update(tree,idx,-1)
            outs.append(m-query(tree,idx))
            update(tree,time,1)
            movie_pos[movie] = time
            time += 1

        print(*outs)
#Fenwick tree functions
def query(a,b):
    pass
def update(tree,idx,value):
    pass

if __name__ == "__main__":
    main()