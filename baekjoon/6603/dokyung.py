from itertools import combinations

def get_combs(a: list):
    combs = list(combinations(a, 6))
    for comb in combs:
        for i in comb:
            print(i, end=' ')
        print()
    print()


lst_list = []

while True:
    lst = list(map(int, input().split()))
    num, cases = lst[0], lst[1:]
    if num == 0:
        break
    elif num > 6 and num < 13:
        cases.sort()
        lst_list.append(cases)

for lst in lst_list:
    get_combs(lst)