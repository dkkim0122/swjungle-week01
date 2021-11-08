# x와 y를 따로 비교하지 말기

x, y, w, h = map(int, input().split())

short = w - x

if x < short:
    short = x

if y < short:
    short = y

if h-y < short:
    short = h-y

print(short)


# short = 0
# x_short = 0
# y_short = 0

# if x > (w - x):
#     x_short = w - x
# else:
#     x_short = x

# if y > (h - y):
#     y_short = h - y
# else:
#     y_short = y

# if x_short > y_short:
#     short = y_short
# else:
#     short = x_short

# print(short)

