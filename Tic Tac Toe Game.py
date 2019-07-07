import random
board = ['$',' ',' ',' ',' ',' ',' ',' ',' ',' ']


def print_board():
    '''Prints the Board in 3*3 matrix format'''
    print(board[7] + '|' + board[8] + '|' + board[9])
    #print(' | | ' )
    print(board[4] + '|' + board[5] + '|' + board[6])
    #print(' | | ')
    print(board[1] + '|' + board[2] + '|' + board[3])


def clear_screen():
     '''Clears the screen'''
     print('\n' * 10)


def take_player_input():
    '''Takes the choice of players whether X or O'''
    inp = True
    while (inp):
        player1 = input("Player1, Enter your choice: ").upper()
        if player1 not in ('X','O'):
            print("Please provide input from 'X' and 'O' only.")
        else:
            if player1 == 'X':
                player2 = 'O'
            else:
                player2 = 'X'
        inp = False
    return player1, player2


def take_pos_input():
           '''Takes the position for input'''
           pos = True
           while (pos):
               position = int(input("Enter the position of your choice(1-9): "))
               if position not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                   #placed = place_marker(board, position1, player1
                   print("Please provide proper input")
                   continue
               else:
                   pos = False
           return position


def check_board_fill():
    '''Checks whether boarad is full or not'''
    if ' ' in board:
        return False
    else:
        return True


def continue_game():
    '''Asks the players wheter they want to play the next game or not'''
    print("Do you want to continue the game: ")
    ans = input()
    if ans == 'Y' or ans == 'y':
        clear_screen()
        clear_board()
        return True
    else:
        return False


def place_marker(board, position, choice):
    '''Places the choice given by player to that number on baord'''
    while (True):
        if board[position] == ' ':
            board[position] = choice
            break
        else:
            print('The mentioned position is already filled, please enter other position.')


def clear_board():
    ''' Clears the entire board'''
    for index in range(1,len(board)):
        board[index] = ' '


def turn():
    '''Randomly defines which player will go first'''
    if random.randint(1,2) == 1:
        return 'Player1'
    else:
        return 'Player2'


def check_game():
    '''Checks whether game has be won or not'''
    if (board[1] == board[2] == board[3] == 'X' or board[1] == board[2] == board[3] == 'O') or (
            board[4] == board[5] == board[6] == 'X' or board[4] == board[5] == board[6] == 'O') or (
            board[7] == board[8] == board[9] == 'X' or board[7] == board[8] == board[9] == 'O') or (
            board[1] == board[4] == board[7] == 'X' or board[1] == board[4] == board[7] == 'O') or (
            board[2] == board[5] == board[8] == 'X' or board[2] == board[5] == board[8] == 'O') or (
            board[3] == board[6] == board[9] == 'X' or board[3] == board[6] == board[9] == 'O') or (
            board[1] == board[5] == board[9] == 'X' or board[1] == board[5] == board[9] == 'O') or (
            board[3] == board[5] == board[7] == 'X' or board[3] == board[5] == board[7] == 'O'):
        return True
    else:
        return False


while not check_board_fill():
    '''Driver code'''
    print("WELCOME TO TIC TAC TOE GAME!!!!")
    player1,player2 = take_player_input()
    turn_first = turn()
    print(turn_first + " will go first")
    game_on = True
    while game_on:
        if turn_first == 'Player1':
            print_board()
            print(turn_first + "'s turn." )
            position = take_pos_input()
            place_marker(board,position,player1)
            if check_game():
                print_board()
                print("Congratulations! Player 1, You won")
                game_on = False
                print("Game Over")
            elif check_board_fill():
                print_board()
                print("Game tie")
            else:
                turn_first = 'Player2'
        else:
            print_board()
            print(turn_first + "'s turn.")
            position = take_pos_input()
            place_marker(board, position, player2)
            if check_game():
                print_board()
                print("Congratulations! Player 2, You won")
                game_on = False
                print("Game Over")
                if not continue_game():
                    break
            elif check_board_fill():
                print_board()
                print("Game tie")
                if not continue_game():
                    break
            else:
                turn_first = 'Player1'
    if not continue_game():
        break
