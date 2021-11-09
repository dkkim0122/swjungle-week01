import sys

N = int(sys.stdin.readline())

pos = [0] * N
flag = [False] * N
flag_1 = [False] * (N * 2 - 1)
flag_2 = [False] * (N * 2 - 1)
count = 0


def set_queen(i):
    # i열에 퀸을 배치하는 함수
    global count
    for j in range(N):
        # j 행에 퀸을 배치하겠다.
        if (not flag[j]
                and not flag_1[i + j]
                and not flag_2[i - j + N - 1]):
            pos[i] = j
            # 만약에 그전까지 flag 와 상관없이 j 행에 퀸을 둘 수 있으면, 둔다.
            if i == N - 1:
                # j 행에 퀸을 뒀을 때, 그것이 마지막 열이었으면, 카운팅(프린트)한다.
                count += 1
                # print(pos)


            else:
                flag[j] = flag_1[i + j] = flag_2[i - j + N - 1] = True
                # 트루라면, i j 행에 퀸을 배치하고 i+1행에 퀸을 배치시작.
                set_queen(i + 1)
                # i + 1, i + 2 ..... i = N-1 까지 다둔다음에 밑에 식 발동.
                flag[j] = flag_1[i + j] = flag_2[i - j + N - 1] = False
                # i 열 j 행에 그냥 안두고 i 행 j 열에 둠.

set_queen(0)
print(count)
