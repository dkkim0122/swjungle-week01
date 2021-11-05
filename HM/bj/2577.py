import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
num = A*B*C
num_ = str(num)
for i in range(10):
    print(num_.count(str(i)))
