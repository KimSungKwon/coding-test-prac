'''
Q 02
곱하기 또는 더하기
'''

data = input()

answer = int(data[0])
for i in range(len(data) - 1):
    if data[i] == '0' or data[i + 1] == '0' or data[i] == '1' or data[i + 1] == '1':
        answer += int(data[i + 1])
    else:
        answer *= int(data[i + 1])

print(answer)
