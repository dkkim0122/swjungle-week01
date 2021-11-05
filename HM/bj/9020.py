import sys

n = int(input())
a = list(int(sys.stdin.readline().rstrip()) for _ in range(n))


def prime(k):
    if k == 1:
        return False
    if k == 2:
        return True
    for p in range(2, k):
        if k % p == 0:
            return False
    return True


for i in a:
    a = []
    for j in range(2, i):
        if prime(j):
            a.append(j)
    x = i // 2
    y = i // 2

    while True:
        if prime(x) and prime(y):
            break
        x -= 1
        y += 1
    print(f'{x} {y}')
