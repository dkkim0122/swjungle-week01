# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# print(f'{a}', end='') == print(a, end='')

import sys

n, x = map(int, input().split())

lst = list(map(int, input().split()))

for a in lst:
    if a < x:
        print(a, end='')
