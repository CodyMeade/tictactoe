
#TIC TAC TOE BOARD
def display_board():
    board = (f'    |   |\n  {place[7]} | {place[8]} | {place[9]}\n ___|___|___\n    |   |\n  {place[4]} | {place[5]} | {place[6]}                    Its your move {player}!\n ___|___|___\n    |   |\n  {place[1]} | {place[2]} | {place[3]}\n    |   |')
    print(board)

#INPUT TO ACCEPT PLAYERS MOVE
def player_input(player):
    global move
    move = int(input(f'Please enter your move {player}'))
    while openpos != ['remaining:']:
        while move not in openpos and move not in range(9):
            print(f'{move} Sorry {move} is not a open position \n(open positions are {openpos}!')
            move = int(input())
        while move in openpos:
            openpos.remove(move)
            global marker
            if player == player1:
                marker = 'X'
            if player == player2:
                marker = 'O'
            return marker
#ASSIGNING PLAYERS MOVE TO THERE MARKER AND PLOTTING ON BOARD
def place_marker(marker, move):
    global place
    place[move]=marker

#CHECKING BOARD FOR WIN OR CAT
def win_check(board, marker):
    win = ''
    while len(win) < 10:
        for i in place:
            if i == marker:
                s = place.index(marker)
                win = win + marker
            else:
                win = win + 'n'
    if win[1] == win[2] == win[3] == 'X' or win[4] == win[5] == win[6] == 'X' or win[7] == win[8] == win[9] == 'X' or win[1] == win[2] == win[3] == 'O' or win[4] == win[5] == win[6] == 'O' or win[7] == win[8] == win[9] == 'O' or place[1] == place[4] == place[7] == marker or place[3] == place[6] == place[9] == marker or place[1] == place[5] == place[9] == marker or place[3] == place[5] == place[7] == marker or place[2] == place[5] == place[8] == marker:
        return True
    if openpos == []:
        return 'cat'

    else:
        return False

#DETERMING WHATS PLAYERS TURN IT IN
def playerup(player):
    if player == player1:
        return player2
    if player == player2:
        return player1
#PROMTING TO PLAY AGAIN OR NOT
def replay():
    global place
    place=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print('Do you want to play tic tac toe?? yes or no')
    global playing
    playing=input().lower()
    return playing == 'yes'

print('Welcome to Tic Tac Toe!')
openpos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playing = 'yes'
player1 = input('Player 1 please enter your name!')
player2 = input('player 2 please enter your name!')
player = playerup(player2)
replay()
display_board()
while playing == 'yes':
    player_input(player)
    place_marker(marker, move)
    win_check(place, marker)
    player = playerup(player)
    display_board()
    if win_check(place, marker) == True:
        print(f'WINNER {playerup(player)}...would you like to replay?')
        replay()
        openpos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if win_check(place, marker) == 'cat':
        print('ITS A CAT!!')
        replay()
        openpos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
else:
    print('Thanks for playing!!!')

