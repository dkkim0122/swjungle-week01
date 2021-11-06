import sys

num_test = int(sys.stdin.readline())

case = []

for i in range(num_test):
    nums = list(sys.stdin.readline().split())
    a1 = int(nums[0])
    a2 = int(nums[1])
    case.append(a1 + a2)

for i in range(num_test):
    print(case[i])
