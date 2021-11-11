import sys
input = sys.stdin.readline

def is_prime(a: int) -> bool:
    if a % 2 == 0:  # 짝수이므로
        return False

    sqr = int(a**(1/2))

    for i in range(2, sqr + 1):
        if a % i == 0:
            return False
    
    return True

def find(n: int) -> list:
    half = n//2

    for i in range(half, 1, -1):
        if is_prime(i) and is_prime(n-i):
            break
    print(i, n-i) 

N = int(input())

for i in range(N):
    a = int(input())
    find(a)