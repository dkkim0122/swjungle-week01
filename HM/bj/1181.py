import sys


# 시간초과
# 줄일방법 생각 : overlap_checklist 불필요 -> 정렬후 출력시 전에 출력한단어와 같지 않을 때 출력하기

def shaker_sort(list_):
    left = 0
    right = len(list_) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if len(list_[j - 1]) > len(list_[j]):
                list_[j - 1], list_[j] = list_[j], list_[j - 1]
                last = j
        left = last

        for k in range(left, right):
            if len(list_[k]) > len(list_[k + 1]):
                list_[k], list_[k + 1] = list_[k + 1], list_[k]
                last = k
        right = last
    print(list_[0])
    for q in range(1, len(list_)):
        if not list_[q - 1] == list_[q]:
            print(list_[q])


N = int(sys.stdin.readline())
overlap_checklist = [None] * N
data_list = [None] * N

for i in range(N):
    data_list[i] = sys.stdin.readline().rstrip()

data_list = sorted(data_list)
shaker_sort(data_list)
