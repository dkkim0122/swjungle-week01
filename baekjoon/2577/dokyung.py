# 빈 리스트를 하나 만들어두고, 
# 나누었을 때 나머지 == 자리의 숫자 에 해당하는 인덱스에 1을 더해 준다.

lst = [0 for i in range(10)] 

a = int(input())
b = int(input())
c = int(input())

multi = a * b * c

while multi != 0:
    num = int(multi % 10)
    multi = multi // 10
    lst[num] += 1

for i in range(10):
    print(lst[i])