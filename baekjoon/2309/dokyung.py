import sys

dwarfs = [None]*9

for i in range(9):
    dwarfs[i] = int(input())

every_sum = sum(dwarfs)

flag = False

for i in range(len(dwarfs)):
    dwarf1 = dwarfs[i]
    for j in range(i+1, len(dwarfs)):
        dwarf2 = dwarfs[j]
        if every_sum - (dwarf1+dwarf2) == 100:
            dwarfs.remove(dwarf1)
            dwarfs.remove(dwarf2)
            flag = True
            break
    if flag == True:
        break

dwarfs.sort()
for i in dwarfs:
    print(i)
