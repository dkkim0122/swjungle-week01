
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

month, day = map(int, input().split())

for_days = 1




for i in range(month - 1):
    for_days += months[i]

for_days += (day-1)

week = for_days % 7

print(days[week])
