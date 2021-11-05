import sys

n = int(input())
a = list(sys.stdin.readline().strip() for _ in range(n))

for i in a:
    index = 0
    hap = 0
    score = 1
    for j in i:
        if i[index] == "O":
            hap += score
            score += 1
        else:
            score = 1
        index += 1
    print(hap)

