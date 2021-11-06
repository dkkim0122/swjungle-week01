a=int(input())
b=int(input())
c=int(input())

#숫자를 문자열로 쪼개기
D=list(str(a*b*c))
# print(a*b*c)
# print(D[0])
N=['0','1','2','3','4','5','6','7','8','9']
n=0
while n<10:
    count = 0
    for i in range(len(D)):
         if D[i]==N[n]:
             count+=1
    else:
        print(count)
        n+=1