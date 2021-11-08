
import sys
input = sys.stdin.readline


def prime(p):
    if p == 1:
        return False
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


a = int(input())
even = list(int(input().strip()) for _ in range(a))  # list 에  a개 만큼 int형 값을 저장


for i in even:
    x = i//2
    y = i//2
    while True:
        if prime(x) and prime(y):
           break
        else:
            x -= 1
            y += 1
    print(x, y)
