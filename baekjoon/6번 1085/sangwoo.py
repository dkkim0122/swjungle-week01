x, y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)
a = (w-x)
b = (h-y)

short_box = [x, y, w, h, a, b]

short = min(short_box)
print(short)