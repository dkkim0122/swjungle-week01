import sys
input = sys.stdin.readline

n = int(input().rstrip())
for i in range(n):
    a = list(input().split())
    k = int(a[0])
    for j in range(len(a[1])):
        print(a[1][j]*k, end="")
    print()



