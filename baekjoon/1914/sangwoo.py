def move(N, x, y):

    if N > 1:
        move(N-1, x, 6-x-y)

    print(f'{x} {y}')

    if N > 1:
        move(N-1, 6-x-y, y)


N = int(input())
count = 2**N - 1
print(count)

if N <= 20:
    move(N, 1, 3)
