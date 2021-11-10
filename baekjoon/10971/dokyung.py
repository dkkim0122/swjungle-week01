from itertools import permutations
import sys
input = sys.stdin.readline

def get_cost(a: list) -> list:
    cost_list = []
    ways = list(permutations(a))

    for way in ways:
        cost = 0
        n = len(way)
        for i in range(n-1):
            cost += w[way[i]][way[i+1]]
        cost += w[way[n-1]][way[0]]
        cost_list.append(cost) 

    return cost_list

N = int(input())

w = [None] * N
a = [i for i in range(N)]

for i in range(N):
    w[i] = list(map(int, input().split()))

cost_list = get_cost(a)

print(min(cost_list))

