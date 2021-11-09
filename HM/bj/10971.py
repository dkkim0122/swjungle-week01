# 1. 가장 적은 비용
# 2. 한번 갔던 도시는 들릴 수 없음, 출발도시로 마지막에 돌아오는거 제외.
# 3. N개의 도시를 모두 거쳐야댐
# 4. 도시들 사이에 길이 없을 수 도있다?

# 입력 :

# 내가 푼 코드 (난잡함)

import sys


def dfs(now, i):
    if i == n - 1:
        # 마지막에 원래 도시로 돌아오는 메소드를 이따 check에 반영해줘야할듯
        path.append([k for k in check])
    else:
        for j in range(0, n):
            if j in check:
                continue
            check[i] = j
            dfs(0, i + 1)
            check[i] = -1


n = int(sys.stdin.readline())
cost = [None] * n
for _ in range(n):
    cost[_] = list(map(int, sys.stdin.readline().split()))
path = []
check = [0] * n
# 0 못들리게 0으로 만듦.
dfs(0, 0)

min_cost = 4000000
# print(path)

for i in range(len(path)):
    hap = 0
    for j in range(len(path[0])):
        if j == 0:
            if cost[0][path[i][0]] == 0:
                hap += min_cost
            else:
                hap += cost[0][path[i][0]]
        else:
            if cost[path[i][j - 1]][path[i][j]] == 0:
                hap += min_cost
            else:
                hap += cost[path[i][j - 1]][path[i][j]]
    min_cost = min(min_cost, hap)
print(min_cost)

# 남이 푼코드
# import sys
#
#
# def move(now, depth):
#     global charge, ans
#     if depth == N:
#         if cost[now][0] > 0:
#             ans = min(ans, charge + cost[now][0])
#         return
#     visit[now] = 1
#     for i in link[now]:
#         # False 일때 실행.
#         if not visit[i]:
#             charge += cost[now][i]
#             move(i, depth + 1)
#             charge -= cost[now][i]
#     visit[now] = 0
#
#
# N = int(sys.stdin.readline())
# cost = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
# visit = [0] * N
# link = {}
# charge, ans = 0, 10 ** 7
#
# for i in range(N):
#     link[i] = []
#     for j in range(N):
#         if cost[i][j] > 0:
#             link[i].append(j)
#
# move(0, 1)
# print(ans)
