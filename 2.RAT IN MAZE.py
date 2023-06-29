def issafe(maze,vis,row,col,n):

    if row>=0 and row<n and col>=0 and col<n and vis[row][col]==False and maze[row][col]==1:
        return True
    return False


def findpathutil(maze,vis,row,col,n):
    if row==n-1 and col==n-1:
        vis[row][col]=True
        return True

    if issafe(maze,vis,row,col,n):

        vis[row][col]=True

        if findpathutil(maze,vis,row+1,col,n):
            return True

        if findpathutil(maze,vis,row,col+1,n):
            return True

        vis[row][col]=False
        return False



def findpath(maze,n):
    vis=[[False for i in range(n)] for j in range(n)]
    if findpathutil(maze,vis,0,0,n):
        for i in range(n):
            for j in range(n):
                if vis[i][j]==True:
                    print(1,end=' ')
                else:
                    print(0,end=' ')
            print()


maze = [ [1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]
findpath(maze,len(maze))

