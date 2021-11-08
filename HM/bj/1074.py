import sys


# N은 1~15
# r 행 c 열은 0부터 시작

def get_num(number, row, col, init):
    case = get_case(number, row, col)
    init += get_init(case, number)
    if number == 1:
        print(init)
    else:
        if case == 1:
            get_num(number - 1, row, col, init)
        elif case == 2:
            get_num(number - 1, row, col - 2 ** (number - 1), init)
        elif case == 3:
            get_num(number - 1, row - 2 ** (number - 1), col, init)
        else:
            get_num(number - 1, row - 2 ** (number - 1), col - 2 ** (number - 1), init)


def get_init(case, layer):
    if layer == 1:
        return case - 1
    else:
        return (2 ** (layer-1))**2 * (case - 1)


def get_case(layer, ver, hor):
    fuck = 2 ** layer
    if 0 <= ver < fuck / 2:
        if 0 <= hor < fuck / 2:
            return 1
        else:
            return 2
    else:
        if 0 <= hor < fuck / 2:
            return 3
        else:
            return 4


N, r, c = sys.stdin.readline().split()
get_num(int(N), int(r), int(c), 0)

# first function
# get case 1 or 2 or 3 or 4


# second function ( get initial number range by first function)
# get new_r and new_r


# fuck*fuck = 2**N * 2**N

# def whereareyou(a, b,N):
