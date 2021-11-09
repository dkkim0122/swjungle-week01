import sys


def shell(a):
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2
    for _ in a:
        print(_)


N = int(sys.stdin.readline())
s = [0] * N
for i in range(N):
    s[i] = int(sys.stdin.readline().rstrip())

shell(s)