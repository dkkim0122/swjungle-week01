# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 굳이 입력받은 N을 가지고 for문을 돌릴 필요는 없다.

import sys

n, x = map(int, input().split())

lst = list(map(int, input().split()))

for a in lst:
    if a < x:
        print(f'{a} ', end='')
