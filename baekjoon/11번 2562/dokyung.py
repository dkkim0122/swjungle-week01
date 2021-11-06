# 자연수들을 받으면서 최댓값을 계속 비교하기. 중간에 몇 번째인지도 수정하기

max = 0
index = 0

for i in range(9):
    a = int(input())
    if a > max:
        max = a
        index = i + 1

print(max)
print(index)