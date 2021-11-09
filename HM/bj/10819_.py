import sys


def dfs(i):
    global answer
    if i == n:
        answer.append([a[tmp] for tmp in tmp_path])
        # answer 리스트 내부에 새로운 리스트로 넣어준다.
    else:
        for j in range(n):
            if j in tmp_path:
                continue
            else:
                tmp_path[i] = j
                dfs(i + 1)
                tmp_path[i] = -1


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
answer = []
tmp_path = [-1] * n
dfs(0)
sexy_num = 0
for i in range(len(answer)):
    max_num = 0
    for j in range(n-1):
        max_num += abs(answer[i][j] - answer[i][j+1])
    sexy_num = max(max_num, sexy_num)

print(sexy_num)
