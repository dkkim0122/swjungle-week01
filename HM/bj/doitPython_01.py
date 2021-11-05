import sys

#
# name = sys.stdin.readline()
# name = int(name)
#
# print(f'안녕하세요 {name} 님')
#
# number = int(sys.stdin.readline())
# hap = 0
# for i in range(1, number + 1):
#     hap += i
#
# print(f'{hap}')

# for _ in range(6):
#     print('+-', end="")

# a = 몇개입력? b = 몇개마다 줄바꿈??

# a, b = map(int, sys.stdin.readline().split())
# for _ in range(a // b):
#     print("*" * b)
# rest = a % b
# if rest:
#     print("*" * rest)


hap = 0
number = int(sys.stdin.readline())
for i in range(1, number + 1):
    hap += i

print(hap)
