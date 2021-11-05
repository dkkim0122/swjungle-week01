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



