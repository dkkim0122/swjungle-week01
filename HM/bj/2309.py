import sys

dwarf_list = [None] * 9
for i in range(9):
    dwarf_list[i] = int(sys.stdin.readline().rstrip())

dwarf_list.sort()
sum_spy = sum(dwarf_list) - 100

for i in range(9):
    spy1 = dwarf_list[i]
    spy2 = sum_spy - dwarf_list[i]

    if spy2 in dwarf_list[i + 1:]:
        dwarf_list.remove(spy1)
        dwarf_list.remove(spy2)
        break
    else:
        continue

for dwarf in dwarf_list:
    print(dwarf)

# for dwarf in dwarf_list:
#     if dwarf != spy1 and dwarf != spy2:
#         print(dwarf)
