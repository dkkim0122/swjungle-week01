# 시험성적
# import sys
# N = int(sys.stdin.readline())
# if N >= 90:
#     print('A')
# elif 80 <= N < 90:
#     print('B')
# elif 70 <= N < 80:
#     print('C')
# elif 60 <= N < 70:
#     print('D')
# else:
#     print('F')

# 윤년
# import sys
# N = int(sys.stdin.readline())
# if N % 4 == 0 and N % 100 != 0 or N % 400 == 0:
#     print(1)
# else:
#     print(0)

# 직사각형 탈출
# import sys
#
# x, y, w, h = map(int, sys.stdin.readline().split())
#
# min_num = w - x
# if min_num > x:
#     min_num = x
# if min_num > h - y:
#     min_num = h - y
# if min_num > y:
#     min_num = y
# print(min_num)

# 구구단
# import sys
# N = int(sys.stdin.readline())
# for j in range(1, 10):
#     print(f'{N} * {j} = {N*j}')

# A + B - 3
# import sys
# N = int(sys.stdin.readline())
# a = []
# for i in range(N):
#     a.append(list(map(int, sys.stdin.readline().split())))
#
# for i in a:
#     print(sum(i))

# 별찍기 틀림 ㅋㅋ
# N = int(input())
# for i in range(N):
#     print('*' * (i+1))

# X보다 작은 수
# import sys
# N, X = map(int, sys.stdin.readline().split())
# a = list(map(int, sys.stdin.readline().split()))
#
# for i in a:
#     if i < X:
#         print(i, end=" ")

# 최댓값
# import sys
#
# a = list(int(sys.stdin.readline().rstrip()) for _ in range(9))
#
# max_num = max(a)
#
# if max_num in a:
#     print(max_num)
#     print(a.index(max_num) + 1)

# OX 퀴즈
# import sys
#
# N = int(sys.stdin.readline())
# a = list(sys.stdin.readline().rstrip() for _ in range(N))
# for i in a:
#     score = 0
#     count = 0
#     for j in i:
#         if j == 'O':
#             count += 1
#             score += count
#         else:
#             count = 0
#     print(score)

# 평균은 넘겠지
# import sys
#
# N = int(sys.stdin.readline())
# a = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
#
# for i in range(N):
#     avg = round(sum(a[i][1:]) / a[i][0],5)
#     count = 0
#     for j in range(1, len(a[i])):
#         if a[i][j] > avg:
#             count += 1
#     print(f'{round(count / a[i][0] * 100, 3):.3f}%')

#  숫자의 개수
# import sys
#
# A = int(sys.stdin.readline().rstrip())
# B = int(sys.stdin.readline().rstrip())
# C = int(sys.stdin.readline().rstrip())
# ABC = str(A*B*C)
# for i in range(10):
#     print(ABC.count(str(i)))

# 아스키 코드
# import sys
#
# a = sys.stdin.readline().rstrip()
# num_board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
# upper_alpha = lower_alpha.upper()
# ascii_num = 0
# if a in num_board:
#     ascii_num = num_board.index(a) + 48
# elif a.isupper():
#     ascii_num = upper_alpha.index(a) + 65
# else:
#     ascii_num = lower_alpha.index(a) + 97
# print(ascii_num)

# 문자열 반복
# import sys
#
# N = int(sys.stdin.readline())
# a = list(list(map(str, sys.stdin.readline().split())) for _ in range(N))
#
# for i in a:
#     for j in range(len(i[1])):
#         print(i[1][j] * int(i[0]), end="")
#     print()

# 단어의 개수
# print(len(input().split()))

# 상수
# import sys
#
# a, b = map(str, sys.stdin.readline().split())
#
# A = int(a[::-1])
# B = int(b[::-1])
# if A > B:
#     print(A)
# else:
#     print(B)

# 달팽이는 올라가고 싶다.
# import sys

#
# up, down, height = map(int, sys.stdin.readline().split())
#
# days = (height - down) // (up - down)
# if (height - down) % (up - down) != 0:
#     days += 1
# print(days)

# 소수찾기
# import sys, math
#
# N = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))
#
#
# def get_prime(i):
#     if i == 1:
#         return False
#     if i == 2:
#         return True
#     if i == 3:
#         return True
#     if i % 2 == 0:
#         return False
#     tennis_num = math.ceil(math.sqrt(i)) + 1
#     for j in range(3, tennis_num, 2):
#         if i % j == 0:
#             return False
#     return True
#
#
# count = 0
# for i in a:
#     if get_prime(i):
#         count += 1
# print(count)

# 골드바흐의 추측
# import sys, math
#
# N = int(sys.stdin.readline())
# a = list(int(sys.stdin.readline().strip()) for _ in range(N))
#
#
# def get_prime(i):
#     if i == 1:
#         return False
#     if i == 2:
#         return True
#     if i == 3:
#         return True
#     if i % 2 == 0:
#         return False
#     tennis_num = math.ceil(math.sqrt(i)) + 1
#     for j in range(3, tennis_num, 2):
#         if i % j == 0:
#             return False
#     return True
#
#
# for i in a:
#     x, y = i // 2, i // 2
#     while True:
#         if get_prime(x) and get_prime(y):
#             print(x, y)
#             break
#         else:
#             x -= 1
#             y += 1

# 한수
# import sys
#
# N = int(sys.stdin.readline())
#
#
# def get_han(hs):
#     if hs < 100:
#         return hs
#     elif hs == 1000:
#         return get_han(999)
#     else:
#         count = 99
#         for i in range(100, hs + 1):
#             tmp = str(i)
#             if int(tmp[0]) - int(tmp[1]) == int(tmp[1]) - int(tmp[2]):
#                 count += 1
#         return count
#
#
# print(get_han(N))

# 종이자르기
# import sys
#
# a, b = map(int, sys.stdin.readline().split())
# T = int(sys.stdin.readline())
# s = list(list(map(int, sys.stdin.readline().split())) for _ in range(T))
# x, y = [0], [0]
# for i in s:
#     if i[0] == 0:
#         x.append(i[1])
#     else:
#         y.append(i[1])
#
# x.sort()
# y.sort()
# x.append(b)
# y.append(a)
# max_x = 0
# max_y = 0
#
# for i in range(1, len(x)):
#     if x[i] - x[i - 1] > max_x:
#         max_x = x[i] - x[i - 1]
# for i in range(1, len(y)):
#     if y[i] - y[i - 1] > max_y:
#         max_y = y[i] - y[i - 1]
# print(max_x * max_y)

# 팩토리얼
# N = int(input())
#
#
# def get_factorial(i):
#     if i == 0:
#         return 1
#     else:
#         return i * get_factorial(i - 1)
#
#
# print(get_factorial(N))

# 하노이 탑
# import sys
#
# N = int(sys.stdin.readline())
# count = 0
#
#
# def get_hanoi(n, a, b, c):
#     global count
#     if n == 1:
#         print(a, c)
#     else:
#         get_hanoi(n - 1, a, c, b)
#         print(a, c)
#         get_hanoi(n - 1, b, a, c)
#
#
# if N > 20:
#     print(2 ** N - 1)
# else:
#     print(2 ** N - 1)
#     get_hanoi(N, 1, 2, 3)

# N-Queen
# import sys
#
# N = int(sys.stdin.readline().rstrip())
# flag = [False] * N
# flag_a = [False] * (N * 2 - 1)
# flag_b = [False] * (N * 2 - 1)
# count = 0
# pos = [0] * N
#
#
# def get_queen(i):
#     global count
#     for j in range(N):
#         if (not flag[j]
#                 and not flag_a[i + j]
#                 and not flag_b[N - 1 - j + i]):
#             pos[i] = j
#             if i == N - 1:
#                 count += 1
#             else:
#                 flag[j] = flag_a[i + j] = flag_b[N - 1 - j + i] = True
#                 get_queen(i + 1)
#                 flag[j] = flag_a[i + j] = flag_b[N - 1 - j + i] = False
#
#
# get_queen(0)
# print(count)

# Z
# import sys
#
#
# def get_z(n, r, c, init):
#     if n == 1:
#         if r == 1:
#             if c == 1:
#                 init += 3
#             else:
#                 init += 2
#         else:
#             if c == 1:
#                 init += 1
#         return init
#     divisor = (2 ** n) // 2
#     if 0 <= r < divisor:
#         if 0 <= c < divisor:
#             return get_z(n - 1, r, c, init)
#         else:
#             init += (2 ** (n - 1)) * (2 ** (n - 1)) * 1
#             return get_z(n - 1, r, c - divisor, init)
#     else:
#         if 0 <= c < divisor:
#             init += (2 ** (n - 1)) * (2 ** (n - 1)) * 2
#             return get_z(n - 1, r - divisor, c, init)
#         else:
#             init += (2 ** (n - 1)) * (2 ** (n - 1)) * 3
#             return get_z(n - 1, r - divisor, c - divisor, init)
#
#
# N, row, col = map(int, sys.stdin.readline().split())
# print(get_z(N, row, col, 0))

# 수정렬하기 1
#  퀵소트~!!!
# import sys
#
# sys.setrecursionlimit(10 ** 6)
# N = int(sys.stdin.readline())
# a = list(int(sys.stdin.readline().strip()) for _ in range(N))
#
#
# def quick_sort(n, left, right):
#     pr = right
#     pl = left
#     mid = n[(left + right) // 2]
#     while pl <= pr:
#         while n[pl] < mid:
#             pl += 1
#         while n[pr] > mid:
#             pr -= 1
#         if pl <= pr:
#             n[pl], n[pr] = n[pr], n[pl]
#             pl += 1
#             pr -= 1
#     if left < pr:
#         quick_sort(a, left, pr)
#     if pl < right:
#         quick_sort(a, pl, right)
#
#
# quick_sort(a, 0, len(a) - 1)
# for i in a:
#     print(i)

# 수 정렬하기 2
# 쉘정렬, 도수정렬

# 수정렬하기 3
# import sys
#
# N = int(sys.stdin.readline())
# board = [0] * 10000
#
# for i in range(N):
#     a = int(sys.stdin.readline().rstrip())
#     board[a - 1] += 1
#
# for i in range(10000):
#     if board[i]:
#         for j in range(board[i]):
#             print(i + 1)
