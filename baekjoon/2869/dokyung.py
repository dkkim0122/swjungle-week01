
climb, fall, height = map(int, input().split())

ratio = (height - fall) / (climb - fall)

if ratio == int(ratio):
    print(int(ratio))
else: print(int(ratio) + 1)