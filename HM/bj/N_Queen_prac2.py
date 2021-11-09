N = int(input())

pos = [0] * N
flag = [False] * N
flag_a = [False] * (N * 2 - 1)
flag_b = [False] * (N * 2 - 1)
count = 0


def recur(i):
    global count
    for j in range(N):
        if (not flag[j]
                and not flag_a[i + j]
                and not flag_b[i - j + N - 1]):
            pos[i] = j
            if i == N - 1:
                count += 1
            flag[j] = flag_a[i + j] = flag_b[i - j + N - 1] = True
            recur(i + 1)
            flag[j] = flag_a[i + j] = flag_b[i - j + N - 1] = False


recur(0)
print(count)
