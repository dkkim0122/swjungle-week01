

def fac(a: int):
    n = 1
    if a == 0:
        n = 1
    else:
        for i in range(1, a+1):
            n *= i
    return n


a = int(input())
print(fac(a))

# 재귀함수로 구하기 재귀함수의 예를 들뿐 효율적이진 않다.
""" 
def fac(n:int)->int:
    if n>0:
        return n*fac(n-1)
    else:
        return 1

n= int(input())
print(fac(n)) """
