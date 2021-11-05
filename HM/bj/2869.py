import sys

up, down, height = map(int, sys.stdin.readline().split())

#  낮에 +A , 밤에 -B, 정상 V
C = up - down

# 5 = 2 % -1 +2 % -1 +2 % -1 +2 = 2(day) + 1*3(day)
days = ((height - up) // C) + 1
if (height - up) % C != 0:
    days += 1

print(days)
