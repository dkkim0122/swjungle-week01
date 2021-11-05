import sys

a = [int(sys.stdin.readline()) for _ in range(9)]
print(sorted(a)[-1])
print(a.index(sorted(a)[-1])+1)
