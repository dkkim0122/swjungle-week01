
climb, fall, height = map(int, input().split())

day = 0

expect = (height - climb) / (climb - fall)

while True:
    day += 1
    if day >= expect:
        print(day + 1)
        break