# 반복문을 3개나 겹치는 건 좀 아닌 거 같다.
# 숫자와 string을 공백으로 구분해서 입력받으려면 어떻게 해야 할까? input().split()

loop = int(input())

for i in range(loop):
    r, s = input().split()
    for j in range(len(s)):
        for k in range(int(r)):
            print(s[j], end='')
        print(end='')
    print()
        

