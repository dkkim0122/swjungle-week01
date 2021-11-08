import sys


def get_hanoi(a, b, c, n):
    if n == 1:
        print(f'{a} {c}')
    if n >= 2:
        get_hanoi(a, c, b, n - 1)
        print(f'{a} {c}')
        get_hanoi(b, a, c, n - 1)


N = int(sys.stdin.readline())
if N > 20: 
    print(2 ** N - 1)
else:
    print(2 ** N - 1)
    get_hanoi(1, 2, 3, N)
