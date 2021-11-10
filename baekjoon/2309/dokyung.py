import sys
from itertools import combinations

dwarfs = [None]*9

for i in range(9):
    dwarfs[i] = int(sys.stdin.readline())

dwarfs.sort()

total_height = sum(dwarfs)

comb = list(combinations(dwarfs, 2))

for dwarf1, dwarf2 in comb:
    if total_height - (dwarf1+dwarf2) == 100:
        dwarfs.remove(dwarf1)
        dwarfs.remove(dwarf2)
        break  # 얘를 안 해줘서 틀렸다라....

for i in dwarfs:
    print(i)