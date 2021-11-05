year = int(input())
num = 0
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    num = 1
print(num)



