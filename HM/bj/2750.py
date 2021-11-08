import sys


def sort_ascend(list_):
    k = 0
    n = len(list_)

    while k < (n - 1):
        last = n - 1
        for j in range(n - 1, k, -1):
            if list_[j - 1] > list_[j]:
                list_[j - 1], list_[j] = list_[j], list_[j - 1]
                last = j
        k = last
    return list_


N = int(sys.stdin.readline())
data_list = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
sorted_list = sort_ascend(data_list)
for _ in sorted_list:
    print(_)