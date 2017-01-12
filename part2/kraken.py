def krakenCount(m, n):
    #create a board, fill the first rows and columns with 0
    board = [[0 for i in range(m)] for row in range(n)]
    #now fill the first row and first column with 1
    for i in range(0, len(board[0])):
        board[0][i] = 1
    for j in range(0, len(board)):
        board[j][0] = 1
    
    #every square is the sum of its upper, left, and upper left neighbors


    return board
