def issafe(x,y,board,n):
    if x>=0 and x<n and y>=0 and y<n and (board[x][y]==-1):
        return True
    return False

def knighttourutil(board,curx,cury,n,move):
    if move>=(n**2):
        return True

    dx=[-2,-2,-1,1,2,2,1,-1]
    dy=[-1,1,2,2,1,-1,-2,-2]

    for i in range(8):
        newx=curx+dx[i]
        newy=cury+dy[i]
        if issafe(newx,newy,board,n):

            board[newx][newy]=move

            if knighttourutil(board,newx,newy,n,move+1):
                return True

            board[newx][newy]=-1
    return False


def knighttour(n):
    board=[[-1 for i in range(n)] for  j in range(n)]
    board[0][0]=0

    print(knighttourutil(board,0,0,n,1))



knighttour(8)

