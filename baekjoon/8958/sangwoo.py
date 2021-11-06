from typing import Sequence

def max(a:Sequence):
    
    maximum = a[0]
    
    for i in range(1, len(a)):
        if a[i]>maximum:
            maximum = a[i]
    return maximum
    
A=[None]*9

for i in range(9):
    A[i]=int(input())

print(max(A), A.index( max(A) )+1, sep='\n')