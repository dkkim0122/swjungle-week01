def z(N, r, c, first_num):
    if N==0:
        return first_num
    
    size = 2**(N-1)  # 4등분한사이즈 4

    if r < size and c < size:
        return z(N-1, r, c, first_num)
    elif r < size and c >= size:
        return z(N-1, r, c % size, first_num + 1 * size**2)
    elif r >= size and c < size:
        return z(N-1, r % size, c, first_num + 2 * size**2)
    else:
        return z(N-1, r % size, c % size, first_num + 3 * size**2)

N, r, c = map(int, input().split())

print(z(N, r, c, 0))




