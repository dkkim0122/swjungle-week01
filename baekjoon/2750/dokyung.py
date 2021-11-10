# 버블 정렬
# 이웃한 두 원소의 대소 관계를 비교해 필요에 따라 교환을 반복하는 알고리즘
from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

if __name__ == "__main__":
    n = int(input())
    lst = [None] * n
    for i in range(n):
        lst[i] = int(input())

    bubble_sort(lst)

    for i in lst:
        print(i)
