A, B, V = map(int, input().split())
a = (V-A) % (A-B)
b = (V-A)//(A-B)

if(a == False):
    print(b+1)
else:
    print(b+2)
