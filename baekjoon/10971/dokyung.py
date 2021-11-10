from itertools import permutations
import sys
input = sys.stdin.readline

def get_cost(a: list) -> list:
    ways = list(permutations(a))
    min = sys.maxsize  #  그냥 정수로서 가장 큰 값 넣어주었다.

    for way in ways:
        if costs[way[-1]][way[0]] == 0:
            continue
        n = len(way)
        cost = 0
        flag = True

        for i in range(n-1):
            camefrom = way[i]
            goto = way[i+1]
            if costs[camefrom][goto] == 0:
                flag = False
                break
            cost += costs[camefrom][goto]
            if cost >= min:
                flag = False
                break
        if flag == False:
            continue 
        cost += costs[way[-1]][way[0]]
        if cost < min:
            min = cost

    return min

N = int(input())

costs = [None] * N
a = [i for i in range(N)]

for i in range(N):
    costs[i] = list(map(int, input().split()))

print(costs)

print(get_cost(a))

