N = int(input())
A=[None]*N
B=[None]*N
for i in range(N):
    a, b=input().split()
    a=int(a)
    b=int(b)
    A[i]=a
    B[i]=b

for i in range(N):
    print(A[i]+B[i])