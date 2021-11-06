# count()함수 사용해보기

lst = [0 for i in range(10)] 

a = int(input())
b = int(input())
c = int(input())

multi = a * b * c

str_multi = str(multi)

for i in range(10):
    print(str_multi.count(str(i)))