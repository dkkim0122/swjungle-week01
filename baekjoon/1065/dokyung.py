def int_to_list(a):
    lst = []
    while a != 0:
        num = a % 10
        a = a // 10
        lst.append(num)
    return lst


def find_han(n):
    if n >= 1 and n < 100:
        return n
    else:
        count = 99
        for i in range(100, n+1):
            a = int_to_list(i)
            if a[1] == (a[0]+a[2])/2:
                count += 1
        
    return count

if __name__ == '__main__':

    n = int(input())

    print(find_han(n))