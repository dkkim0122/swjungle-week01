# 소수인지를 찾는 함수?
def find_prime(a):
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


n = int(input())

lst = list(map(int, input().split()))

count = 0

for i in range(n):
    if find_prime(lst[i]) == True:
        count += 1
    
print(count)

