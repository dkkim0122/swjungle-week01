import sys


def get_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * get_factorial(n - 1)


N = int(sys.stdin.readline())
print(get_factorial(N))
