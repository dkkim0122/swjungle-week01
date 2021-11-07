n = int(input())
is_prime = [False, False] + [True]*(n-1)    # 0과 1은 소수가 아니다
primes = []

sq = int(n**0.5)

for i in range(2, sq+1):
    if is_prime[i]:    # 만약 해당 숫자가 소수이면 소수 리스트에 추가한다.
        primes.append(i)
        for j in range(2*i, n+1, i):    # 그리고 해당 숫자(소수)의 배수들은 모두 소수가 아니다.
            is_prime[j] = False
print(primes)
