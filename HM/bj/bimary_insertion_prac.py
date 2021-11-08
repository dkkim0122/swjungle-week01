def b_prac(sequence):
    n = len(sequence)
    for i in range(1, n):
        j = i
        tmp = sequence[i]
        while j > 0 and sequence[j - 1] > tmp:
            sequence[j] = sequence[j - 1]
            j -= 1
        sequence[j] = tmp
