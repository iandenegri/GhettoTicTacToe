from IPython.display import clear_output

win_state = False

def play():
    # Give players the rules.
    print('Claim a tile by inputting the tile # you want, 1-9. Tiles are numbered from left to right, top to bottom.')
    turns = 1
    s1 = ['`']
    s2 = ['-']
    s3 = ['`']
    s4 = ['-']
    s5 = ['`']
    s6 = ['`']
    s7 = ['-']
    s8 = ['`']
    s9 = ['-']
    board = [0, s1, s2, s3, s4, s5, s6, s7, s8, s9]

    def win_check(board):
        ''' Check Horizontals,Verticals, and Diagonals for a win '''
        if (board[7] == board[8] == board[9]) or \
                (board[4] == board[5] == board[6]) or \
                (board[1] == board[2] == board[3]) or \
                (board[7] == board[4] == board[1]) or \
                (board[8] == board[5] == board[2]) or \
                (board[9] == board[6] == board[3]) or \
                (board[1] == board[5] == board[9]) or \
                (board[3] == board[5] == board[7]):
            return True
        else:
            return False

    def player1(tile):
        # Allows player 1 to claim a square
        board[int(tile)].clear()
        board[int(tile)].append(0)

    def player2(tile):
        # Allows player 2 to claim a square
        board[int(tile)].clear()
        board[int(tile)].append(5)

    def gameboard():
        # Creates the game board in a 3x3 format
        print(board[1] + board[2] + board[3])
        print(board[4] + board[5] + board[6])
        print(board[7] + board[8] + board[9])

    # create the game board.
    while turns < 5:
        clear_output()
        gameboard()
        print('Player 1, it\'s your turn!!!')
        player1(input('please pick where you want to claim a spot \n'))
        print('Player 2, it\'s your turn now!!!!')
        player2(input('please pick where you want to claim a spot \n'))
        turns += 1
        # Check for player win
        if win_check(board):
            win_state = True
            if win_state == True:
                gameboard()
                break
    print('good game')


play()
