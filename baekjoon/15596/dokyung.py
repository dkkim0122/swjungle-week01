lst = list(map(int, input().split()))

print(lst)

def solve(a: list) -> int:
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum

print(solve(lst))
