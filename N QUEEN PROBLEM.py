def issafe(board,row,col,n):
    for i in range(4):
        if board[i][col]==1:
            return False
    i=row
    j=col

    while(i>=0 and j>=0):
        if board[i][j]==1:
            return False
        i-=1
        j-=1

    i = row
    j = col

    while(i>=0 and j<n):
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    return True


def findqueenutil(board,row,n):

    if row>=n:
        return True

    for col in range(4):
        if issafe(board,row,col,n):

            board[row][col]=1

            if findqueenutil(board,row+1,n):
                return True
            board[row][col]=0
    return False


def findnqueen():
    n=4
    board=[[0 for i in range(n)] for j in range(n)]
    if findqueenutil(board,0,n):
        for i in range(4):
            for j in range(4):
                if board[i][j]==1:
                    print('Q',end=' ')
                else:
                    print(board[i][j],end=' ')
            print()



findnqueen()