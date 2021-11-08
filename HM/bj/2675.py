# import sys
# input = sys.stdin.readline
#
# n = int(input().rstrip())
# for i in range(n):
#     a = list(input().split())
#     k = int(a[0])
#     for j in range(len(a[1])):
#         print(a[1][j]*k, end="")
#
#
#
#
#     print()
#
case = int(input())
test = [None] * case

for i in range(case):
    test[i] = list(input().split())
    test[i][0] = int(test[i][0])  # split으로 나누면 숫자도 str로 들어가기때문에 int로 해당위치 변경

""" print(type(test[0][0])) """

for n in range(case):
    a = len(test[n][1])

    for i in range(a - 1):

        print(test[n][1][i] * test[n][0], end='')
    else:
        print(test[n][1][(a - 1)] * test[n][0], sep='\n')
