# 1. 가장 적은 비용
# 2. 한번 갔던 도시는 들릴 수 없음, 출발도시로 마지막에 돌아오는거 제외.
# 3. N개의 도시를 모두 거쳐야댐
# 4. 도시들 사이에 길이 없을 수 도있다?

# 입력 :

import sys


def dfs(i):
    global path

    if i == n - 1:
        # 마지막에 원래 도시로 돌아오는 메소드를 이따 check에 반영해줘야할듯

        path.append([k for k in check])
    else:
        for j in range(0, n):
            if j in check:
                continue
            check[i] = j
            dfs(i + 1)
            check[i] = -1


n = int(sys.stdin.readline())
cost = [None] * n
for _ in range(n):
    cost[_] = list(map(int, sys.stdin.readline().split()))
path = []
check = [0] * n
# 0 못들리게 0으로 만듦.
dfs(0)

min_cost = 4000000
print(path)

for i in range(len(path)):
    hap = 0
    for j in range(len(path[0])):
        if j == 0:
            hap += cost[0][path[i][0]]
        else:
            hap += cost[path[i][j - 1]][path[i][j]]
    print(hap)
    min_cost = min(min_cost, hap)
print(min_cost)
# print(cost)
