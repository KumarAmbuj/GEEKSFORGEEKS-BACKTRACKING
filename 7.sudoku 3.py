def issafe(board,row,col,num,n):
    for i in range(n):
        if board[row][i]==num:
            return False
    for j in range(n):
        if board[j][col]==num:
            return False
    x=row-row%3
    y=col-col%3
    for i in range(x,x+3):
        for j in range(y,y+3):
            if board[i][j]==num:
                return False
    return True


def fillsudoku(board,row,col,n):
    if row==n:
        return True

    if col==n:
        return fillsudoku(board,row+1,0,n)

    if board[row][col]!=0:
        return fillsudoku(board,row,col+1,n)

    for num in range(1,10):
        if issafe(board,row,col,num,n):

            board[row][col]=num

            if fillsudoku(board,row,col+1,n):
                return True

            board[row][col]=0
    return False


def sudoku(board,n):
    if fillsudoku(board,0,0,n):
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=' ')
            print()
    else:

        print('not possible')

grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
sudoku(grid,9)