
from typing import MutableSequence

def insertion_sort(lst: MutableSequence) -> None:
    n = len(lst)

    for i in range(1, n):
        j = i
        temp = lst[i]
        while j > 0 and len(lst[j-1]) > len(temp):
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = temp


n = int(input())
lst = [None]*n

for i in range(n):
    lst[i] = input()

lst.sort()
insertion_sort(lst)

print(lst[0])
for i in range(1, len(lst)):
    if not lst[i-1] == lst[i]:
        print(lst[i])