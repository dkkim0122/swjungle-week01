# 1번 2557 문제
""" print('Hello World!') """

# 2번 10869 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

""" 
A, B = input().split() #split 으로 a와 b를 한번에 입력받을경우 나누어 저장
A = int(A)
B = int(B)

print(A+B, A-B, A*B, A//B, A%B, sep='\n') #sep \n 으로 줄바꾸어 표기 
"""

# 3번 2558 (첫재 줄에 세자리 자연수 둘째줄에 세자리 자연수가 주어질때 각 세자리 곱셈의 연산과정 보여주기)
""" 
A=int(input()) #입력값을 정수로 저장
B=str(input()) #입력값을 문자열로 저장
print(A*int(B[-1]), A*int(B[-2]), A*int(B[-3]), A*int(B), sep='\n') #문자열인 B를 int형으로 변환하여 A와 곱한다.
 """

# 4번 9498 (시험성적)

"""
A= int(input())

if 100>=A>=90:
    print('A')
elif 89>=A>=80:
    print('B')
elif 79>=A>=70:
    print('C')
elif 69>=A>=60:
    print('D')
else :
    print('F')

 """

# 5번 2753(윤년)

"""
year=int(input())

if ((year%4==0)and(year%100 != 0))or(year%400==0):
    print(1)
else: print(0)

"""
# 6번 1085(직사각형 탈출)

""" x, y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)
a = (w-x)
b = (h-y)

short_box = [x, y, w, h, a, b]

short = min(short_box)
print(short) """

# 7번 2739(구구단)

""" N=int(input())
for i in range(1,10):
    print(f'{N} * {i} = {N*i}') """


# 8번 10950(A+b-3) 두 정수를 입력받아 덧셈 표현

""" N = int(input())
A=[None]*N
B=[None]*N
for i in range(N):
    a, b=input().split()
    a=int(a)
    b=int(b)
    A[i]=a
    B[i]=b

for i in range(N):
    print(A[i]+B[i])
 """
# 9번 2438 별찍기

""" N=int(input())

for i in range(N):
    for _ in range(i+1):
     print('*',end='')
    print() """

# 10번 10871 x보다 작은수 찾기
""" 
N, X = map(int,input().split())
L = list(map(int,input().split())) #list(map(함수, 리스트)

for i in range(N):
    if L[i] <X:
        print(L[i],end=' ')
 """

# 11번 8958 최댓값 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오

""" from typing import Sequence

def max(a:Sequence):
    
    maximum = a[0]
    
    for i in range(1, len(a)):
        if a[i]>maximum:
            maximum = a[i]
    return maximum
    
A=[None]*9

for i in range(9):
    A[i]=int(input())

print(max(A), A.index( max(A) )+1, sep='\n') """

# 12번 8958 ox퀴즈
""" 
N=int(input())
test=[None]*N

def OXscore(A):
    a=len(A)
    i=0
    Ocount = 0
    score =0

    while i<=a-1:
     if A[i]=='O':
        Ocount +=1
        score += Ocount
        i += 1
     else:
        Ocount = 0
        i+= 1
    return score

for i in range(N):
   test[i]=input('')
for i in range(N):
    print(OXscore(test[i]))

 """

# 13번 4344 평균은 넘겠지

""" cls = int(input())
SCORE = [None]*cls

for i in range(cls):
    SCORE[i]=list(map(int,input().split()))

def avg(a):
    sum =0
    for i in range(1,len(a)):
        sum += a[i]

    average=sum/a[0]

    return average
def per(a):
    count=0
    for i in range (1,len(a)):
        if a[i]>avg(a):
            count+=1
    percentage = round(count/a[0]*100,3)
    return percentage
    
for i in range(cls):
 print(f'{format(per(SCORE[i]),".3f")}%')
 """

# 14번 2577 숫자의 개수

""" a=int(input())
b=int(input())
c=int(input())

#숫자를 문자열로 쪼개기
D=list(str(a*b*c))
# print(a*b*c)
# print(D[0])
N=['0','1','2','3','4','5','6','7','8','9']
n=0
while n<10:
    count = 0
    for i in range(len(D)):
         if D[i]==N[n]:
             count+=1
    else:
        print(count)
        n+=1
 """

# 15번 15596번 정수 N개의 합
""" 
a = [1,2,3]

def solve(a: list) -> int:
    sum=0
    for i in range (len(a)):
        sum += a[i]
    return sum

print(solve(a)) """

# 16번 11654 아스키코드
""" 
n = input()
print(ord(n)) #ord() 입력된 문자를 아스키 코드값으로 반환, chr() 아스키코드를 문자로 반환
 """

# 17번 2675 문자열 반복

""" case = int(input())
test = [None]*case

for i in range (case):
    test[i] = list(input().split())
    test[i][0]=int(test[i][0]) #split으로 나누면 숫자도 str로 들어가기때문에 int로 해당위치 변경

for n in range(case):
    a=len(test[n][1])

    for i in range(a-1):

        print(test[n][1][i]*test[n][0],end='')
    else: print(test[n][1][(a-1)]*test[n][0], sep='\n')
 """

# 18번 1152번 단어의 개수

""" a=input().split()
print(len(a))
 """

# 19번 2908번 상근이동생 상수

""" 

a,b=input().split()
a=int(a[::-1])
b=int(b[::-1])

if a>b:
    print(a)
else : 
    print(b)

"""

# 20번 2869 달팽이는 올라가고 싶다.

""" 
A, B, V = map(int,input().split())
a = (V-A)%(A-B)
b = (V-A)//(A-B)

if(a==False):
    print(b+1)
else:
    print(b+2)     """

# 21번 1987번 소수찾기
""" import sys
input = sys.stdin.readline

n = int(input())
y=list(map(int,input().split()))
count = 0

def prime(a):
    if a==1:
        return False
    for i in range(2,a):
        if a%i == 0 :
           return False
    else: return True


for i in range(n):
    if prime(y[i])==True:
        count +=1
print(count) """


# 리스트 안에서 값의 갯수를 찾기
""" x = [1, 1, 2, 4, 5, 6, 6, 6, 7, 6, 7, 8, 9]
y = [6,7,1]
print()
count = 0
for i in range(len(y)):
    a=x.count(y[i])
    if a != 0:
     count += a
print(count) """

# 22 9020 골드바흐의 추측 https://www.acmicpc.net/problem/9020


""" import sys
input = sys.stdin.readline

def prime(p):
    if p==1:
        return False
    for i in range(2,p):
        if p%i==0:
            return False 
    return True

a = int(input())
even = list(int(input().strip()) for _ in range(a)) #list 에  a개 만큼 int형 값을 저장


for i in even:
    x=i//2
    y=i//2
    while True:
        if prime(x) and prime(y) :
           break
        else :
            x-=1
            y+=1
    print(x,y)
 """

# 23번 한수 https://www.acmicpc.net/problem/1065

import sys
input = sys.stdin.readline


def hansu(N):
    count = 0

    for i in range(1, N+1):
        n = list(map(int, str(i)))

        if 1 <= i < 100:
            count += 1
        elif n[1] == (n[2]+n[0])/2:
            count += 1
    return count


N = int(input())
print(hansu(N))
