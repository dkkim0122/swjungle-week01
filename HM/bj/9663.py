import sys


def get_queen(n):
    if n == N:
        global count
        count += 1
    else:
        for i in range(N):
            board[n] = i
            if checker(n):
                get_queen(n + 1)


def checker(n):
    for i in range(n):
        if (board[n] == board[i]) or (n - i == abs(board[n] - board[i])):
            return False
    return True


N = int(sys.stdin.readline())
count = 0
board = [0] * N
get_queen(0)
print(count)
