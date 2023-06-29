def issafe(maze,row,col,n,vis):
    if row>=0 and row<n and col>=0 and col<n and maze[row][col]!=0 and vis[row][col]==0:
        return True
    return False

def findpathutil(maze,row,col,vis,n):
    if row==n-1 and col==n-1:
        return True

    dx=[0,1]
    dy=[1,0]

    d=maze[row][col]

    for i in range(2):

        for j in range(1,d+1):
            x=row+dx[i]*j
            y=col+dy[i]*j

            if issafe(maze,x,y,n,vis):

                vis[x][y]=1

                if findpathutil(maze,x,y,vis,n):
                    return True
                vis[x][y]=0
    return False






def findpath(maze,n):
    vis=[[0 for i in range(n)] for j in range(n)]
    vis[0][0]=1

    if findpathutil(maze,0,0,vis,n):
        for i in range(n):
            for j in range(n):
                print(vis[i][j],end=' ')
            print()
    else:
        print('no')

maze = [[2, 1, 0, 0],
        [3, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 1]]
findpath(maze,4)