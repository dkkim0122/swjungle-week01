def move(n: int, x: int, y: int) -> int:

    if n > 1:
        move(n-1, x, 6-x-y)
    
    print(x, y)

    if n > 1:
        move(n-1, 6-x-y, y)

n = int(input())

count = 2**n - 1
print(count)

if n <= 20:
    move(n, 1, 3)
