# 선형 탐색(보초법)

import copy

def bin_search(a: list, key: int) -> int:
    n = len(a)
    pl = 0
    pr = n - 1

    while pl <= pr:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return 1        
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
    return 0


n = int(input())
n_list = list(map(int, input().split()))
n_list_sorted = sorted(n_list)

m = int(input())
m_list = list(map(int, input().split()))

for i in range(len(m_list)):
    result = bin_search(n_list_sorted, m_list[i])
    print(result)
