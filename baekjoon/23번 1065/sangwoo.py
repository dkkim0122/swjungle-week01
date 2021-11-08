import sys
input = sys.stdin.readline


def hansu(N):
    count = 0

    for i in range(1, N+1):
        n = list(map(int, str(i)))

        if 1 <= i < 100:
            count += 1
        elif n[1] == (n[2]+n[0])/2:
            count += 1
    return count


N = int(input())
print(hansu(N))
