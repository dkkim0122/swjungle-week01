# 리스트와 언팩
""" x=[1,2,3]
a,b,c=x
print(a)
print(b)
print(c)
print(a, b, c) """

# 2-2 78page 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence #Any는 제약없는 임의의 자료형을 의미한다, Sequence는 시퀀스형을 의미한다.

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

