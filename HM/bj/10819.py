# import sys
#
#
# def spider(list_):
#     mid = len(list_) // 2
#     left = 0
#     right = len(list_) - 1
#     hap = 0
#     last = list_[mid]
#     count = 1
#     flag = True
#     # True -> left need to be added
#
#     while count < len(list_):
#         if flag:
#             hap += abs(last - list_[left])
#             last = list_[left]
#             left += 1
#             count += 1
#             flag = False
#         else:
#             hap += abs(last-list_[right])
#             last = list_[right]
#             right -= 1
#             count += 1
#             flag = True
#     return hap
#
#
# N = int(sys.stdin.readline())
#
# a = list(map(int, sys.stdin.readline().split()))
#
# a.sort()
# print(spider(a))


# 이문제는 backtrackiing, bruteforce algorithm


# def dfs(depth):
#     if depth == N:
#         res.append(sum(abs(li[i + 1] - li[i]) for i in range(N - 1)))
#         return
#     for i in range(N):
#         if check[i]:
#             continue
#         li.append(nums[i])
#         check[i] = 1
#         dfs(depth + 1)
#         li.pop()
#         check[i] = 0
#
#
# N = int(input())
# nums = list(map(int, input().split()))
# li, res = [], []
# check = [0] * N
# dfs(0)
# print(max(res))

from sys import stdin


def dfs(depth):
    global answer

    if depth == n:
        answer.append([nums[i] for i in check])
    else:
        for i in range(n):
            if i in check:
                continue
            check[depth] = i
            dfs(depth + 1)
            check[depth] = -1


if __name__ == '__main__':
    answer = []
    n = int(stdin.readline())
    nums = sorted(list(map(int, stdin.readline().split())))
    check = [-1] * n
    dfs(0)
    min_case = 0
    for case in answer:
        sum_case = 0
        for i in range(n - 1):
            sum_case += abs(case[i] - case[i + 1])
        min_case = max(min_case, sum_case)
    print(min_case)
