
def is_prime(a:int) -> bool:
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def prime_list(a:int) -> list:
    lst = []
    if a == 1:
        return lst    
    for i in range(2, a + 1):
        if is_prime(i) == True:
            lst.append(i)
    return lst

loop = int(input())

for i in range(loop):
    n = int(input())
    small_primes = prime_list(n//2)
    max = 0

    for i in range(len(small_primes)):
        small = small_primes[i]
        big =  n - small

        if is_prime(big) == True:
            if small > max:
                max = small

    print(f'{max} {n-max}')
    