A=int(input()) #입력값을 정수로 저장
B=str(input()) #입력값을 문자열로 저장
print(A*int(B[-1]), A*int(B[-2]), A*int(B[-3]), A*int(B), sep='\n') #문자열인 B를 int형으로 변환하여 A와 곱한다.