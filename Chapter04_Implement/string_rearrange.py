'''
Q 08 문자열 재정렬
'''

data = list(input())
data.sort()

# 알파벳이 시작되는 index를 찾아 index에 저장
index = 0
for i in range(len(data)):
    if ord(data[i]) >= 65:
        index = i
        break;

# 0부터 index 이전까지의 값(숫자)들의 합을 number에 저장
number = 0
for i in range(0, index):
    number += int(data[i])

# 알파벳들을 출력, 그 후 number 출력
for i in range(index, len(data)):
    print(data[i], end='')

print(number)
