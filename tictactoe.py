# variables to hold board and each players symbol
board = ['#'] + [' '] * 9
player1 = ''
player2 = ''
cur_player = ''
# variable used to determine if the game has been won
won = False
moves = 0


# print blank line to clear board off screen
def clear_board():
    print('\n' * 100)


# print current board to console
def print_board():
    print('  ' + ' ! ' + ' ' + ' ! ' + '  ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---' + '|' + '---' + '|' + '---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---' + '|' + '---' + '|' + '---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('  ' + ' ! ' + ' ' + ' ! ' + '  ')


# function to represent a players move
def fill_square(player, position):
    global moves
    if check_move(position):
        board[position] = player
        moves += 1
        check_won(player)
        end_move(player)


# check player move is valid
def check_move(position):
    if position in range(1, 10):
        if board[position] == ' ':
            return True
    print('Invalid move')
    return False


# switch control to next player
def end_move(player):
    global cur_player
    if player == 'X':
        cur_player = '0'
    else:
        cur_player = 'X'


# function to check if the game has been won
def check_won(player):
    global won
    line = [player] * 3
    # check for filled horizontal lines
    if board[1:4] == line or \
       board[4:7] == line or \
       board[7:] == line or \
       board[1:8:3] == line or \
       board[2:9:3] == line or \
       board[3::3] == line or \
       (board[1] == player) and (board[5]) == player and (board[9]) == player or \
       (board[3] == player) and (board[5]) == player and (board[7]) == player:
        print(f'Player {player} wins!')
        won = True


# function to represent a move by the player
def player_move(player):
    try:
        fill_square(player, int(input(f'Player {player} move: ')))
        print_board()
    except ValueError:
        print('Invalid move')


# pick player symbols
while player1 == '':
    # available symbols
    symbols = ['X', '0']
    player1 = input('Player 1 pick symbol').upper()
    # ask for symbol again if not X or 0
    if player1 not in symbols:
        print('Symbols may only be X or 0')
        player1 = ''
        continue
    symbols.remove(player1)
    player2 = symbols[0]

# player symbols picked, start game
print('-----Start Game-----')
print(f'Player 1 is: {player1}')
print(f'Player 2 is: {player2}')
print('Player 1 goes first')
# set player to the current player
cur_player = player1
print_board()

# ask for player move
while not won:
    if not won and moves < 9:
        player_move(cur_player)
    # board filled so game is a draw
    if moves == 9:
        print('It\'s a draw!')
        won = True