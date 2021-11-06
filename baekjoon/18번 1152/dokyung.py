# 문자열은 공백으로 시작하거나 끝날 수 있다. -> wordflag 사용

s = input()
count = 0
wordflag = False

for i in range(len(s)):
    if wordflag == False and s[i] != ' ':
        wordflag = True
        count += 1
    elif wordflag == True and s[i] == ' ':
        wordflag = False

print(count)