def countBattleships(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X':
                if (i == len(board) - 1 or board[i + 1][j] == '.') and (j == len(board[0]) - 1 or board[i][j + 1] == '.'):
                    count += 1
    return count
