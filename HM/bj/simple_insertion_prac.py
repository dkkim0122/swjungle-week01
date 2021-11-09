data = [1, 4, 6, 7, 3, 9, 8]

for i in range(1, len(data)):
    j = i
    tmp = data[j]
    # 템프에 삽입되는 숫자를 저장해놓고 while 문이 끝나면 (j가 계속 마이너스돼어서 삽입될 곳의 인덱스가 j 가됨, 거기에 저장해놓았던 템프입력)
    while j > 0 and data[j - 1] > tmp:
        data[j] = data[j - 1]
        j -= 1
    data[j] = tmp

print(data)