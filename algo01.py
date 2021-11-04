print('get sum of int from a to b')
a = int(input('enter in a : '))
b = int(input('enter in b : '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):
    if i < b:
        print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end='')
sum += b

print(sum)