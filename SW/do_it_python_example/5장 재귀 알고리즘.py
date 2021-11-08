# 5-2 유클리드 호재법 gcd 최대공약수 구하기

""" def gcd(x:int,y:int)->int:
    if y==0:
        return x
    else :
        return gcd(y,x%y)

x,y = map(int,input().split())

print(gcd(x,y))
 """

# 5-3 하노이탑

def move(N, x, y):

    if N > 1:
        move(N-1, x, 6-x-y)

    print(f'{x} {y}')

    if N > 1:
        move(N-1, 6-x-y, y)


N = int(input())

print(move(N, 1, 3,))
