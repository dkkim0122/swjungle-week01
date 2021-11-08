def factorial(a : int) -> int:
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)

if __name__ == '__main__':
    n = int(input())
    print(factorial(n))