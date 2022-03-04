'''
Q 03 
문자열 뒤집기

다시 풀기
'''
s = list(map(int, input()))

flip0 = 0
flip1 = 0

if s[0] == 1:
    flip0 += 1
else:
    flip1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == 0:
            flip0 += 1
        else:
            flip1 += 1

print(min(flip0, flip1))
