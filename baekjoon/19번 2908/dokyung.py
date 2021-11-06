
def reassem(a:int) -> int:
    lst =[]
    i = 0
    while a != 0:
        rest = a % 10
        a = a // 10
        lst.append(rest)
        i += 1

    length = len(lst)

    num = 0
    for i in range(length):
        num += lst[length - i - 1] * pow(10, i)
    return num

def larger(a:int, b:int):
    if a >= b:
        return a
    else:
        return b

a, b = map(int, input().split())

a1 = reassem(a)
b1 = reassem(b)

print(larger(a1, b1))