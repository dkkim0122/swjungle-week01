A = int(input())
B = int(input())

b1 = int(str(B)[2])
b2 = int(str(B)[1])
b3 = int(str(B)[0])

print(A * b1)
print(A * b2)
print(A * b3)
print(A * B)

num2 = B % 10
num3 = (B - num2) / 10 % 10
num4 = B // 100

print(A * num2)
print(A * num3)
print(A * num4)
print(A * B)

