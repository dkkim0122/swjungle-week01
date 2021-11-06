# 리스트와 언팩
""" x=[1,2,3]
a,b,c=x
print(a)
print(b)
print(c)
print(a, b, c) """

# 2-2 78page 시퀀스 원소의 최댓값 출력하기

""" from typing import Any, Sequence #Any는 제약없는 임의의 자료형을 의미한다, Sequence는 시퀀스형을 의미한다.

def max_of(a: Sequence) -> Any: #건네받은 a의 자료형은 시퀀스형이며 반환값은 임의의 자료형이다.

    # 시퀀스형 a원소의 최댓값을 반환"
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__=='__main__': #__name__ 모듈이름(2장 기본자료구조와 배열) 이지만 최초로 실행된 스크립트 파일의 __name__에는 __main__ 이 들어가기때문에 참으로 판별 if를 실행한다.
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요.:'))
    x=[None]*num #원소 수가 num개인 리스트 생성 

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.:'))
    
    print(f'최댓값은{max_of(x)}입니다.')

 """

#  2-4 배열의 원소값을 난수로 결정하기

""" import random
from max import max_of

print('난수의 최댓값을 구한다.')

num = int(input('난수의 개수를 입력하시오.:'))
lo = int(input('난수의 최솟값을 입력하시오:'))
hi = int(input('난수의 최댓값을 입력하시오:'))

x = [None]*num

for i in range(num):
    x[i] = random.randint(lo, hi) #lo 이상 hi이하인 정수형 난수 반환

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.') """

# 2C-1 리스트의 모든 원소를 스캔하기(원소 수를 미리 파악)
 
""" x=['snagwoo', 'Gorge', 'Yujin']

for i in range(len(x)):
    print(f'x[{i}] ={x[i]}')


y=['snagwoo', 'Gorge', 'Yujin']

for i, name in enumerate(x):         #enumerate() 함수는 인덱스와 원소를 짝찌어 튜플로 꺼내는 내장함수이다. 
    print(f'x[{i}] ={x[i]}')
 """

# 2-4 리스트 역순으로 정렬하기

""" x=[1,2,3]
x.reverse() #리스트 x의 원소를 역순으로 정렬
print(x)

y=list(reversed(x)) #다시 역순으로 정렬해 y로 참조
print(y) """

# 리스트 값의 위치(인덱스)찾기

x=[1,2,3,5,6,7]
print(x.index(3)+1) #단순히 인덱스만 찾으면 0부터 시작해서 1이 작음