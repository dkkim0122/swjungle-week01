# # idea
#
# # 1. 일단, (1, 100) 까지 해봐야댐. 참고, N = 2 이상, 100이하. -> DFS
# # 처음부터 탐색함. h(높이가 주어졌을때) 큰걸 만나면 check
# # 다음라인으로 넘어감
# #
#
# import sys
#
# N = int(sys.stdin.readline())
# zone = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
# flag = list(list(False for _ in range(N)) for _ in range(N))
# count = [0] * N
# to_be_checked = []
#
# def get_flag(a, h):
#     n = len(a)
#     for i in range(n):
#         for j in range(n):
#             if a[i][j] > h:
#                 flag[i][j] = True
#
# for i in range(len(zone)):
#     for j in range(len(zone)):
#
#

# x = 1
# y = -1
# queue = collections.deque()
# queue.append((x, y))
# print(queue)
# print(x,y)
# x, y = queue.popleft()
# print(queue)
# print(x,y)
# arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# # for k in range(max(map(max, arr))):
# #     print(k)
# print(arr.pop(), end=" ")
# print(arr)
#
# a, b =[1, 2]
# print(a, b)
#
#
# a = [1,2]


import collections
import sys


def bfs(x, y, height):
    q = collections.deque()
    q.append((x, y))
    count = 1
    while q:
        a, b = q.popleft()
        flag[a][b] = True
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if zone[nx][ny] > height and flag[nx][ny] == False:
                    q.append((nx, ny))
                    flag[nx][ny] = True
                    count += 1
    return count


N = int(sys.stdin.readline())
zone = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_height = max(map(max, zone))
max_safeZone = 0

for k in range(max_height + 1):
    flag = list([False] * N for _ in range(N))
    result = []
    for i in range(N):
        for j in range(N):
            if zone[i][j] > k and not flag[i][j]:
                result.append(bfs(i, j, k))
    max_safeZone = max(max_safeZone, len(result))

print(max_safeZone)
