import sys

n = int(input())
a = [sys.stdin.readline().split() for i in range(n)]

for i in range(n):
    print(int(a[i][0]) + int(a[i][1]))

