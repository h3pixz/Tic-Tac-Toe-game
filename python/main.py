import random


def display_board(board):
    print('-------------')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('-------------')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('-------------')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('-------------')


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Игрок 1, выберите X или O: ').upper()
    player1 = marker
    player2 = 'O' if player1 == 'X' else 'X'
    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    return any(all(board[i] == mark for i in combination) for combination in winning_combinations)


def choose_first():
    return random.choice(['Игрок 1', 'Игрок 2'])


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return all(board[i] != ' ' for i in range(1, 10))


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Выберите позицию(1-9): '))
    return position


def replay():
    choice = input('Желаете сыграть еще? Напишите Да или Нет: ')
    return choice.lower() == 'Да'


def play_tic_tac_toe():
    print('Добро пожаловать в игру Крестики Нолики')
    while True:
        the_board = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' будет первым.')
        play_game = input('Вы готовы играть? Нажмите д или н: ')
        if play_game.lower() == 'д':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Игрок 1':
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)

                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print('Игрок 1 выиграл!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('TIE GAME!')
                        game_on = False
                    else:
                        turn = 'Игрок 2'
            else:
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Игрок 2 выиграл!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('TIE GAME!')
                        game_on = False
                    else:
                        turn = 'Игрок 1'

        if not replay():
            if play_game.lower() == 'n':
                print('Пока! Хорошего дня.')
            else:
                print('Спасибо за тест моей игры.')
            break


# Start the game
play_tic_tac_toe()