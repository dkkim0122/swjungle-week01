def find_han(n):
    count = 0

    for i in range(1, n+1):
        a = list(map(int, str(i)))
        if i >= 1 and i < 100:
            count += 1
        elif a[1] == (a[0]+a[2])/2:
            count += 1
            
    return count

if __name__ == '__main__':

    n = int(input())

    print(find_han(n))