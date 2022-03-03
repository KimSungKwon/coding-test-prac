'''
Q 02
곱하기 또는 더하기
'''

data = list(map(int, input()))

result = data[0]

for i in range(0, len(data)-1):
    if data[i] == 0:
        result += data[i+1]
    else:
        result *= data[i+1]
        
print(result)
