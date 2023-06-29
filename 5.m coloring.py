def issafe(adj,v,color,c,n):
    for i in range(n):
        if adj[v][i]==1 and color[i]==c:
            return False
    return True


def coloring(adj,v,m,n,color):
    if v==n:
        return True
    for c in range(1,m+1):
        if issafe(adj,v,color,c,n):
            color[v]=c
            if coloring(adj,v+1,m,n,color):
                return True
            color[v]=-1
    return False



def findcolor(adj,n,m):
    color=[-1 for i in range(n)]

    if coloring(adj,0,m,n,color):
        print(color)

graph = [[0, 1, 1, 1],
           [1, 0, 1, 0],
           [1, 1, 0, 1],
           [1, 0, 1, 0]]
m = 3
findcolor(graph,4,m)
