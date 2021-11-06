def max_of_list(a:list) -> int:
    max = 0
    for i in range(len(a) - 1):
        if (a[i+1] - a[i]) > max:
            max = a[i+1] - a[i]
    return max

def make_list(a:list):
    lst = []
    for i in range(len(a)):
        if a[i] != 0:
            lst.append(a[i])
    return lst

if __name__ =='__main__':
    a, b = map(int, input().split())

    n = int(input())

    x = [0 for _ in range(a + 1)]
    y = [0 for _ in range(b + 1)]
    x[a] = a
    y[b] = b
    
    for i in range(n):


        x_or_y, num = map(int, input().split())

        if x_or_y == 1:
            x[num] = num
        elif x_or_y == 0:
            y[num] = num


    x1 = make_list(x)
    y1 = make_list(y)

    area = max_of_list(x1) * max_of_list(y1)

    print(area)

