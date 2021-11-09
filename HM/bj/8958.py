import sys

N = int(sys.stdin.readline())
a = list(sys.stdin.readline().rstrip() for _ in range(N))
for i in a:
    score = 0
    count = 0
    for j in i:
        if j == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)

# import sys
#
# n = int(input())
# a = list(sys.stdin.readline().strip() for _ in range(n))
#
# for i in a:
#     index = 0
#     hap = 0
#     score = 1
#     for j in i:
#         if i[index] == "O":
#             hap += score
#             score += 1
#         else:
#             score = 1
#         index += 1
#     print(hap)


