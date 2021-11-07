# 테스트 케이스 개수를 입력받으면 그 개수만큼 for문을 돌린다. 
import sys
input = sys.stdin.readline

n = int(input())
lst = list(input().strip() for _ in range(n))

for a in lst:
    score = 0
    add_score = 0

    for i in range(len(a)):
        if a[i] == 'O':
            score += 1
            add_score += score
        else:
            score = 0
    print(add_score)
    