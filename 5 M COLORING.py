def issafe(v,adj,n,c,color):
    for i in range(n):
        if adj[v][i]==1 and color[i]==c:
            return False
    return True

def coloring(v,adj,m,n,color):
    if v==n:
        return True

    for c in range(1,m+1):
        if issafe(v,adj,n,c,color):
            color[v]=c
            if coloring(v+1,adj,m,n,color):
                return True
            color[v]=-1
    return False

def find(adj,n,m):
    color=[-1 for i in range(n)]

    if  coloring(0,adj,m,n,color):
       print('possible')
       print(color)

graph = [[0, 1, 1, 1],
           [1, 0, 1, 0],
           [1, 1, 0, 1],
           [1, 0, 1, 0]]
m = 3
find(graph,4,m)

