# 테스트 케이스 개수를 입력받으면 그 개수만큼 for문을 돌린다. 
# flag 활용???
n = int(input())

for i in range(n):
    lst = list(input())
    flag = False

    score = 0
    add_score = 0
    total = 0


    for i in range(len(lst)):
        if flag == False and lst[i] == 'O':
            flag = True
            score += 1
            add_score += score
        elif flag == True and lst[i] == 'O':
            score += 1
            add_score += score
        elif flag == True and lst[i] == 'X':
            flag = False
            total += add_score
            score = 0
            add_score = 0

    total += add_score

    print(total)

