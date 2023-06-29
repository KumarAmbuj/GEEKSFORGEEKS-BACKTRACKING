def issafe(board,row,col,n):

    for i in range(n):
        if board[row][i]==1:
            return False
    i=row
    j=col

    while(i>=0 and j>=0):
        if board[i][j]==1:
            return False
        i-=1
        j-=1

    i=row
    j=col

    while(i<n and j>=0):
        if board[i][j]==1:
            return False
        i+=1
        j-=1

    return True


def findnqueenutil(board,col,n):
    if col>=n:
        return True

    for row in range(n):
        if issafe(board,row,col,n):

            board[row][col]=1

            if findnqueenutil(board,col+1,n):
                return True

            board[row][col]=0
    return False

def findnqueen(n):
    board=[[0 for i in range(n)] for j in range(n)]

    if findnqueenutil(board,0,n):
        for i in range(n):
            for j in range(n):
                if board[i][j]==1:
                    print('Q',end=' ')
                else:
                    print(board[i][j],end=' ')
            print()

findnqueen(4)