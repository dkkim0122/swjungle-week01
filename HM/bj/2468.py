import sys


def to_flag(a, n):
    row = len(a)
    for j in range(row):
        for k in range(len(a[j])):
            if a[j][k] <= n:
                a[j][k] = False
            else:
                a[j][k] = True

    return a


def count_bunker(a, n):
    last = a[0][0]
    hap = 0
    for k in a:
        hap += k.count(True)
    count = 0
    linecheck = -1
    t = 0
    # right_checker(i, j), left_checker(i, j), head_checker(linecheck, rowcheck),
    while count < hap:
        for i in a:
            linecheck += 1
            rowcheck = -1
            for j in range(len(i)):
                rowcheck += 1
                if i[j]:
                    last = i[j]
                    t += 1
                    continue
                if not i[j]:
                    if last != i[j]:
                        index = j



def right_checker(a, i):
    m = len(a) - 1
    if i == m:
        return True
    elif not a[i + 1]:
        return True
    else:
        return False


def left_checker(a, i):
    if i == 0:
        return True
    elif not a[i - 1]:
        return True
    else:
        return False


def head_checker(r, c):
    # 몇행 몇열?
    global g
    if r == 0:
        return True
    elif not g[r + 1][c]:
        return True
    else:
        return False


def bot_checker(r, c):
    global g
    if r == len(g) - 1:
        return True
    elif not g[r - 1][c]:
        return True
    else:
        return False


def checking_tool(i, j):
    holy = []
    if True:
        holy.append([0, 1])


""" 
1. n = 100 이면 count = 0
idea :
True -> need to be checked (keep going) 
폴스 만나면 인덱스 체크하고 (체크포인트)
다음 줄으로 이동, 

   
    
"""

N = int(input())
data_list = [None] * N
for i in range(N):
    data_list[i] = list(map(int, sys.stdin.readline().split()))

# print(to_flag(data_list, 4))
g = to_flag(data_list, 4)
c = 0
for i in g:
    c += i.count(True)
print(c)
# print([True, True, False].count(True))
