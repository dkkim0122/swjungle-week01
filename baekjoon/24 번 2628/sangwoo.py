
def max(a: list):
    max = 0
    for i in range(1, len(a)):
        if a[i]-a[i-1] > max:
            max = a[i]-a[i-1]
    return max


x, y = map(int, input().split())
N = int(input())
X = [0, x]  # 가로
Y = [0, y]  # 세로

for i in range(N):
    a = list(map(int, input().split()))
    if a[0] == 0:
        Y.append(a[1])
    else:
        X.append(a[1])

X.sort()
Y.sort()

print(max(X)*max(Y))
