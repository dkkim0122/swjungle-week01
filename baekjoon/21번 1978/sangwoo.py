import sys
input = sys.stdin.readline

n = int(input())
y = list(map(int, input().split()))
count = 0


def prime(a):
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
           return False
    else:
        return True


for i in range(n):
    if prime(y[i]) == True:
        count += 1
print(count)
