import sys


def get_ari_seq(n):
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])
    if a == b and b == c:
        return True
    if not a < b < c:
        if not a > b > c:
            return False
    if abs(a - b) == abs(b - c):
        return True


N = int(sys.stdin.readline())
count = 0
if 0 < N < 100:
    count = N
for i in range(100, N + 1):
    if get_ari_seq(str(i)):
        count += 1
count += 99
print(count)
