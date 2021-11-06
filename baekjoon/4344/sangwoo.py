cls = int(input())
SCORE = [None]*cls

for i in range(cls):
    SCORE[i]=list(map(int,input().split()))

def avg(a):
    sum =0
    for i in range(1,len(a)):
        sum += a[i]

    average=sum/a[0]

    return average
def per(a):
    count=0
    for i in range (1,len(a)):
        if a[i]>avg(a):
            count+=1
    percentage = round(count/a[0]*100,3)
    return percentage
    
for i in range(cls):
 print(f'{format(per(SCORE[i]),".3f")}%')