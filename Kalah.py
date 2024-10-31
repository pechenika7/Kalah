from random import randint
def game_over(b):
    winner = randint(0, 3)
    return winner

def next_move(b, k):
    pass
    return b, k

def new_game():
    board = list()
    board.append(list())
    board.append(list())
    for i in range(6):
        board[0].append(6)
        board[1].append(6)
    board[0].append(0)
    board[1].append(0)
    return board

def draw_board(b):
    print(b[1][0:6])
    print(b[1][6], '              ', b[0][6])
    print(b[0][0:6])

print("Hello. I'm programm Kalah!")
board = new_game()
while True:
    draw_board(board)
    k = 0  # номер ходящего
    board, k = next_move(board, k)
    if game_over(board) == 0:
        print('First player win')
        break
    elif game_over(board) == 1:
        print('Second player win')
        break
    elif game_over(board) == 2:
        print('Draw')
        break
    else:
        print('Game continue')