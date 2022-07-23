from os import system


import os

def invite():                                                                   # function to invite player/s to play
    response = ''
    accept = ['YES', 'Yes', 'yes']
    decline = ['NO', 'No', 'no']
    while response not in accept and response not in decline:
        response = input('Do you want to play Tic Tac Toe? (Type Yes or No)     ')
        if response not in accept and response not in decline:
            os.system('clear')
            print("Type Yes or No; it's not rocket science")
    os.system('clear')
    return response in accept

def x_or_o():                                                                   # function to ask player to choose X or O
    players = {'one': '', 'two': ''}
    while players['one'] not in ['X', 'O', 'x', 'o']:
        players['one'] = input('Choose your poison: type X or O     ')
        if players['one'] not in ['X', 'O', 'x', 'o']:
            os.system('clear')
            print('really? type X or O')
    os.system('clear')
    players['one'] = players['one'].upper()
    if players['one'] == 'X':
        players['two'] = 'O'
    else:
        players['two'] = 'X'
    os.system('clear')
    return players

def printer(board):                                                                    # function to print board on screen
    print('\t\t    Welcome to the Board \n\n\t\t  Choose your moves wisely.\n\n\n')
    print(f'\t\t\t {board[0]} | {board[1]} | {board[2]}''\n'
          '\t\t\t-----------\n'
          f'\t\t\t {board[3]} | {board[4]} | {board[5]}''\n',
          '\t\t\t-----------\n'
          f'\t\t\t {board[6]} | {board[7]} | {board[8]}''\n''\n''\n')


def player_move(players, board,):                                                    # function that makes moves on board and returns a winner
    player_one = players['one']
    player_two = players['two']
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    print('\t\t'f'Player one is {player_one} and Player two is {player_two}''\n\n')
    winner = ''
    count = 0
    while not winner:
        os.system('clear')
        printer(board)

        if not count % 2:
            print('Player one make your move\nChoose a number on the board')
            one_response = 0
            while (one_response not in range(1,10) and
            (board[one_response - 1] != 'X' or board[one_response - 1] != 'O')):
                try:
                    one_response = int(input("(>'.')> player One    "))
                except ValueError:
                    os.system('clear')
                    printer(board)
                    print('seriously?')
            board[one_response - 1] = player_one
            count += 1
            os.system('clear')
            printer(board)
            for lst in wins:
                num = 0
                for idx in lst:
                    if board[idx] == player_one:
                        num += 1
                if num == 3:
                    winner = 'Player One'
                    return winner
            if count == 9:
                break

        if count % 2:
            print('Player two make your move\nChoose a number on the board')
            two_response = 0
            while (two_response not in range(1,10) and
            (board[two_response - 1] != 'X' or board[two_response - 1] != 'O')):
                try:
                    two_response = int(input("(>'.')> player Two    "))
                except ValueError:
                    os.system('clear')
                    printer(board)
                    print('seriously?')
            board[two_response - 1] = player_two
            count += 1
            os.system('clear')
            printer(board)

            for lst in wins:
                counter = 0
                for idx in lst:
                    if board[idx] == player_two:
                        counter += 1
                if counter == 3:
                    winner = 'Player Two'
                    return winner

    if not winner:
        print('\t\t\tYOU BOTH LOSE!')


def play_xo():                                                                  # function to initiate game, announce winner and ask to play again
    positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    game = invite()
    if game:
        result = player_move(x_or_o(), positions)
        if result:
            print('\t\t  'f'Winner, winner: {result}\n\n')

        game = invite()


play_xo()                                                                       # invoke function to run game
