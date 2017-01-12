def krakenCount(m, n):
    #edge cases
    if m==0 or n==0:
        return 0

    #create a board, fill the first rows and columns with 0
    board = [[0 for i in range(m)] for row in range(n)]
    #now fill the first row and first column with 1
    for i in range(0, len(board[0])):
        board[0][i] = 1
    for j in range(0, len(board)):
        board[j][0] = 1
    
    #every square is the sum of its upper, left, and upper left neighbors
    #go by rows and fill in each one
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            #add the upper, left, and upper left squares
            board[i][j] = board[i-1][j] + board[i][j-1] + board[i-1][j-1]

    #return the bottom right corner
    return board[n-1][m-1]
