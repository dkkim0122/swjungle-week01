N=int(input())
test=[None]*N

def OXscore(A):
    a=len(A)
    i=0
    Ocount = 0
    score =0

    while i<=a-1:
     if A[i]=='O':
        Ocount +=1
        score += Ocount
        i += 1
     else:
        Ocount = 0
        i+= 1
    return score

for i in range(N):
   test[i]=input('')
for i in range(N):
    print(OXscore(test[i]))