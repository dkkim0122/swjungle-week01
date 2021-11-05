import sys

A = sys.stdin.readline().split()
A[0] = A[0][::-1]
A[1] = A[1][::-1]
print(max(int(A[0]), int(A[1])))
