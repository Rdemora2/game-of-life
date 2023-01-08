import os
from time import sleep
from logics import board, see_board

def game():
    game_board = board()
    try:
        while True:
            print(game_board)
            sleep(0.5)
            os.system('clear')
            sgame_board = see_board(game_board)
    except KeyboardInterrupt:
        print('\n\nJogo interrompido!')

game()