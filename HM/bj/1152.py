import sys

A = input()
hap = A.count(" ")+1
if A.startswith(" "):
    hap -= 1
if A.endswith(" "):
    hap -= 1
print(hap)


B = sys.stdin.readline().strip()
if B == "":
    print(0)
else:
    print(len(B.split(" ")))

