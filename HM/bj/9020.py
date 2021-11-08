
import sys, math

n = int(input())
a = list(int(sys.stdin.readline().rstrip()) for _ in range(n))


def prime(k):
    if k == 1:
        return False
    if k == 2:
        return True
    if k == 3:
        return True
    if k % 2 == 0:
        return False
    else:
        tennis = math.ceil(math.sqrt(k)) + 1
        for p in range(3, tennis, 2):
            if k % p == 0:
                return False
    return True


for i in a:

    x = i // 2
    y = i // 2

    while True:
        if prime(x) and prime(y):
            break
        x -= 1
        y += 1
    print(f'{x} {y}')
