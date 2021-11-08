import sys

C = int(input())

for i in range(C):
    a = list(map(int, sys.stdin.readline().split()))
    avg = sum(a[1:]) / a[0]
    count = 0
    for j in range(1, len(a)):
        if a[j] > avg:
            count += 1
    print("{:.3f}%".format(round((count / (len(a) - 1) * 100), 3)))

# import sys
# input = sys.stdin.readline
#
# test_case = int(input())
#
# for _ in range(test_case):
#     data = input().strip().split(' ')
#     scores = list(map(float, data[1:]))
#     average = sum(scores) / len(scores)
#
#     above = 0
#     for score in scores:
#         if score > average:
#             above += 1
#
#     print(f'{(above/len(scores))*100:.3f}%')