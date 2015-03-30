import copy

field = [['0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0']]

user_board = copy.deepcopy(field)


def reset_field():
    for i, row in enumerate(field):
        for j, col in enumerate(row):
            if col != 0:
                field[i][j] = 0


def print_board(board):
    for i in board:
        print ' '.join(i)
