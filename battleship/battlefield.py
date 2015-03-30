import random
import board



def _generate_ship_position():
    x = random.randint(0, 5)
    y = random.randint(0, 5)
    return x, y


def locate_ship():
    i = 10
    while i > 0:
        x, y = _generate_ship_position()
        if not ship_in_pos(x, y):
            board.field[y][x] = 1
            i -= 1


def ship_in_pos(x, y):
    return board.field[y][x] == 1


def attack_ship(x, y):
    if ship_in_pos(x, y) and not board.field[y][x] == 'X':
        board.field[y][x] = 'X'
        board.user_board[y][x] = 'X'
        return True

    board.user_board[y][x] = '1'
    return False


def guess_location():
    turn = 0
    while True:
        board.print_board(board.user_board)
        row = int(raw_input('guess coordinate x:')) - 1
        col = int(raw_input('guess coordinate y:')) - 1
        try:
            if not attack_ship(row, col):
                wrong_guess(row, col)
                turn += 1
                if turn >= 5:
                    print 'Game Over'
                    break
            else:
                print "Arr! You hit me!"
        except IndexError:
            print "Oops, that's not even in the ocean. Try again"


def wrong_guess(x, y):
    if not board.field[y][x] == 'X':
        print "You missed it!"
    elif board.field[y][x] == 'X':
        print "You already made that guess. Try again:"

if __name__ == '__main__':
    locate_ship()
    guess_location()
