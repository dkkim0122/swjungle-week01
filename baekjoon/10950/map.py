# map()을 이용해서 코드 간결하게 줄이기.

import sys

num_test = int(sys.stdin.readline())

case = []

for i in range(num_test):
    nums = list(map(int, sys.stdin.readline().split()))
    case.append(nums[0] + nums[1])

for i in range(num_test):
    print(case[i])
