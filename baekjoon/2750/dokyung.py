from typing import MutableSequence


def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):  # 두 번째 원소부터 시작
        j = i   # j는 앞으로 비교하게 될 원소의 인덱스
        temp = a[i]  # temp에 넣고
        while j > 0 and a[j-1] > temp:  # 앞의 원소가 더 작으면 스탑.
            a[j] = a[j-1]   # 원래 원소 자리를 하나씩 오른쪽으로 메우고
            j -= 1    # 하나씩하나씩
        a[j] = temp  # 빈 해당 자리에 temp값을 넣어준다.


if __name__ == "__main__":
    n = int(input())
    lst = [int(input().strip()) for _ in range(n)]

    insertion_sort(lst)

    for i in lst:
        print(i)
