import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))


def prime(k):
    if k == 1:
        return False
    if k == 2:
        return True
    for p in range(2, k):
        if k % p == 0:
            return False
    return True


count = 0
for i in a:
    if prime(i):
        count += 1
print(count)
