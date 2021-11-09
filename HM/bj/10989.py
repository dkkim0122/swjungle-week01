import sys

N = int(sys.stdin.readline())
a = [0] * 10000
for i in range(N):
    b = int(sys.stdin.readline().rstrip())
    a[b - 1] += 1

for j in range(10000):
    if a[j]:
        for k in range(a[j]):
            print(j + 1)