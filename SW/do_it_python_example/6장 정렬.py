#6-1 버블 정렬 알고리즘 구현
""" from typing import MutableSequence

def bubble_sort(a:MutableSequence)->None:
    n=len(a)

    for i in range(n-1):
        exchange = 0
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchange +=1
        if exchange == 0:
            break


if __name__=='__main__':
    print('버블 정렬을 수행합니다.')
    
    num=int(input('원소 수를 입력하세요.: '))

    x=[None]*num #원소 수가 num 인 배열을 생성

    for i in range(num):
        x[i]=int(input(f'x[{i}]:'))
    
    bubble_sort(x)

    print('오름차순으로 정렬했습니다.')

    for i in range(num):
        print(f'x[{i}] = {x[i]}') """

#6-11퀵 정렬 알고리즘 (재귀적)
""" 
from typing import MutableSequence

def qsort(a : MutableSequence, left:int, right:int) ->None:

    pl = left
    pr = right
    x= a[(left + right)//2] #피벗(가운데 원소)

    while pl<=pr:
        while a[pl] < x : pl+=1
        while a[pr] > x : pr-=1

        if pl<=pr:
            a[pl],a[pr]=a[pr],a[pl]
            pl+=1
            pr-=1
    #위의 반복문을 마친 pr은 반을 넘어온 (left + right)//2-1의 값 pl은 반대로 반을 넘은값
    if left<pr : qsort(a,left,pr) # 좌우 각 그룹을 다시 나누기 위해 재귀호출
    if pl<right: qsort(a,pl,right)

def quick_sort(a:MutableSequence)->None:
    qsort(a,0,len(a)-1)


if __name__ == '__main__':

    num = int(input('원소 수를 입력하세요.: '))

    x = [None]*num  # 원소 수가 num 인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))

    quick_sort(x)

    print('오름차순으로 정렬했습니다.')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')

 """
 