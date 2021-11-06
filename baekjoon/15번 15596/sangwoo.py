a = [1,2,3]

def solve(a: list) -> int:
    sum=0
    for i in range (len(a)):
        sum += a[i]
    return sum

print(solve(a))