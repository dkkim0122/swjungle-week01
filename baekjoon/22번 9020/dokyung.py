import sys
input = sys.stdin.readline

num = 10000

is_prime = [False, False] + [True]*(num-1)
for i in range(2, num + 1):
    if is_prime[i] == True:
        for j in range(i * 2, num+1, i):
            is_prime[j] = False

repeat = int(input())

for i in range(repeat):
    n = int(input())
    half = n//2

    for j in range(half, 1, -1):
        if is_prime[j] == True and is_prime[n-j] == True:
            print(j, n - j)
            break
