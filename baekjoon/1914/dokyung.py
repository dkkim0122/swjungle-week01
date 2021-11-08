
g_count = 0
lst = []

def move_under_20(n: int, x: int, y: int) -> int:
    global g_count
    global lst

    if n > 1:
        move_under_20(n-1, x, 6-x-y)
    
    move = (x, y)
    lst.append(move)
    g_count += 1

    if n > 1:
        move_under_20(n-1, 6-x-y, y)
    
def move_over_20(n: int, x: int, y: int) -> int:
    global g_count

    if n > 1:
        move_over_20(n-1, x, 6-x-y)
    
    g_count += 1

    if n > 1:
        move_over_20(n-1, 6-x-y, y)
    

n = int(input())

if n > 20:
    move_over_20(n, 1, 3)
    print(g_count)
else:
    move_under_20(n, 1, 3)
    print(g_count)
    for a in lst:
        print(a[0], a[1])

