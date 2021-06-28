import random
def display_board(board):

    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    marker=""

    while not (marker== 'X' and marker== 'O'):
        marker=input("Player 1: Choose between 'X' or 'O' : ").upper()

    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

player1_marker,player2_marker= player_input()

def place_maker(board,marker,position):
    board[position]=marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    flip= random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'

#print(f'player 1 is {player1_marker}')
#print(f"player2 is {player2_marker}")



def space_check(board,position):
    return board[position]==" "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a postion: (1-9):'))
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No :').lower().startswith('y')

print("Welcome to the Tic Tak Toe")
print(" By Nitin")
while True:
    #reset the board
    the_board = [' ']*10
    player1_marker,player2_marker=player_input()
    turn= choose_first()
    print(turn+ " will go first")

    play_game= input("Ready to play? y or n?")
    if play_game=='y':
        game_on = True
    else:
        game_on = False
    ##Game play
    while game_on:
        if turn== 'Player 1':
            #Show the board to the player
            display_board(the_board)

            #Choose a position
            position = player_choice(the_board)

            #Place the marker on the positon
            place_maker(the_board,player1_marker,position)

            #Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player1 has won')
                game_on= False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("its a tie")
                    game_on= False
                else:
                    turn= 'Player 2'

            #check for a tie

            #No tie no win next players turn

        else:

                # Show the board to the player
                display_board(the_board)

                # Choose a position
                position = player_choice(the_board)

                # Place the marker on the positon
                place_maker(the_board, player2_marker, position)

                # Check if they won
                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Player2 has won')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("its a tie")
                        game_on = False
                    else:
                        turn = 'Player 1'

    if not replay():
        break
#display_board(the_board)

