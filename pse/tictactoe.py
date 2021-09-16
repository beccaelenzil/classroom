def tictactoe(board):

    # check for row win
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]

    # check for col win
    for j in range(3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j]:
            return board[0][j]

    # check for diag win
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    # check for tie or incomplete
    count = 0
    for row in board:
        for element in row:
            if element != '':
                count += 1
    
    if count == 9:
        return 'Tie'

    return None
    
#tie 
print(tictactoe([
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'X', 'O']
]))

#incomplete 
print(tictactoe([
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', '', 'O']
]))

#row 
print(tictactoe([
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'O', 'O']
]))

#column 
print(tictactoe([
    ['X', 'O', 'X'],
    ['O', 'O', 'O'],
    ['X', 'X', 'O']
]))

#diagonal
print(tictactoe([
    ['O', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'X', 'O']
]))


        