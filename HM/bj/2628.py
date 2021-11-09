# 0 -> 가로
# 1 -> 세로

# 10 8
# 3
# 0 3
# 1 4
# 0 2

import sys

x, y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
cut_list = [sys.stdin.readline().split() for _ in range(N)]

ver = [0]
hor = [0]

for i in cut_list:
    if i[0] == '0':
        ver.append(int(i[1]))
    else:
        hor.append(int(i[1]))
ver.append(y)
hor.append(x)

ver.sort()
hor.sort()
new_ver = []
new_hor = []


for i in range(0, len(ver) - 1):
    new_ver.append(ver[i + 1] - ver[i])
for i in range(0, len(hor) - 1):
    new_hor.append(hor[i + 1] - hor[i])

print(max(new_ver)*max(new_hor))
