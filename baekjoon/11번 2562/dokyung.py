# 자연수들을 받으면서 최댓값을 계속 비교하기. 중간에 몇 번째인지도 수정하기

import sys
input = sys.stdin.readline

a = [int(input()) for _ in range(9)]

# 정렬한 다음 마지막 요소가 최댓값
# a라는 이터러블 객체를 작은 수부터 정렬한 다음
# 마지막([-1]) 인덱스의 요소를 골라낸다.
max = sorted(a)[-1]

# 리스트.index(요소) : 해당 값을 갖고 있는 요소의 인덱스 값을 반환
index = a.index(max) + 1

print(max)
print(index)
