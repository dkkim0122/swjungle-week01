x, y, w, h = map(int, input().split())

mini = w - x

if mini >= x:
    mini = x

if mini >= y:
    mini = y

if mini >= h - y:
    mini = h - y

print(mini)
