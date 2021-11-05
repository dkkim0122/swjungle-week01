
line = int(input())
for i in range(line):
    sum = 0
    count = 0

    lst = list(map(int, input().split()))
    n = lst[0]

    for i in range(1, n+1):
        sum += lst[i]
    avg = float(sum / n)

    for i in range(1, n+1):
        if lst[i] > avg:
            count += 1

    ratio = (count / n) * 100
    print('{:.3f}%'.format(ratio))

