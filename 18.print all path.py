def issafe(row,col,maze,m,n):
    if row>=0 and row<m and col>=0 and col<n:
        return True
    return False

def findpathutil(maze,row,col,m,n,path):
    if row==m-1 and col==n-1:
        print(path)
        return

    dx=[0,1]
    dy=[1,0]

    for i in range(2):
        x=row+dx[i]
        y=col+dy[i]
        if issafe(x,y,maze,m,n):

            path.append(maze[x][y])

            findpathutil(maze,x,y,m,n,path)

            path.pop()

def findpath(maze,m,n):
    path=[]
    path.append(maze[0][0])

    findpathutil(maze,0,0,m,n,path)

mat = [[1, 2, 3],
       [4, 5, 6]]
findpath(mat,2,3)