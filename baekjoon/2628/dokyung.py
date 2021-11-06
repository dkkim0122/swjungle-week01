# 리스트.sort()를 사용하면 리스트 내 원소들을 정렬할 수 있다.

def max_of(a:list):
    max = 0
    for i in range(1, len(a)):
        if a[i] - a[i-1] > max:
            max = a[i] - a[i-1]
    return max

if __name__ =='__main__':
    a, b = map(int, input().split())

    n = int(input())

    x = [0, a]
    y = [0, b]

    for i in range(n):
        x_or_y, num = map(int, input().split())

        if x_or_y == 1:
            x.append(num)
        elif x_or_y == 0:
            y.append(num)

    x.sort()
    y.sort()

    area = max_of(x) * max_of(y)

    print(area)

