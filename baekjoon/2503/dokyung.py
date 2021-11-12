# 랜덤으로 서로 다른 세개의 숫자들 순열들 만든 다음
# 매 트라이마다 주어진 숫자와 strike, ball 판단해서
# 입력받은 결과와 다르면 지운다.
from itertools import permutations

def strike_ball(num:str, case:list) -> list:
    strike_count = 0
    ball_count = 0

    flag = [False] * 3

    # 형변환을 해 주어야 한다. 
    # num 안의 각 숫자들은 str, case 안의 각 숫자들은 int이다.
    for i in range(len(num)):
        if int(num[i]) == case[i]:
            flag[i] = True
            strike_count+=1
        if flag[i] == False:
            if int(num[i]) in case:
                ball_count += 1
    
    return strike_count, ball_count


cases = list(permutations(range(1,10), 3))
    
n = int(input())

trials = [None]*n
check = [True] * len(cases)

for i in range(n):
    trials[i] = list(input().split())

for trial in trials:
    num = trial[0]
    strike = int(trial[1])
    ball = int(trial[2])

    for i in range(len(cases)):
        result = strike_ball(num, cases[i])
        if (result[0] != strike) or (result[1] != ball):
             check[i] = False
            
print(sum(check))