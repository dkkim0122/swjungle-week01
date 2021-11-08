import sys

N = int(sys.stdin.readline())
overlap_checklist = [None] * N
data_list = [None] * N

for i in range(N):
    data_list[i] = sys.stdin.readline().rstrip()


print(data_list)

# ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']