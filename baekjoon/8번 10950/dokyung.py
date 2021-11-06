import sys

num_test = int(sys.stdin.readline())

case = []

for i in range(num_test):
    nums = list(map(int,sys.stdin.readline().split()))
    
    case.append(nums[0] + nums[1])
"""     a1 = int(nums[0])
    a2 = int(nums[1])
    case.append(a1 + a2)
""" 
for i in range(num_test):
    print(case[i])
