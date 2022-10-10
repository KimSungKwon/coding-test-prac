"""
Q32 정수 삼각형
"""

n = int(input())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

# data[i][j] = max(data[i-1][j-1] + @, data[i-1][j] + @)
for i in range(1, n):
    for j in range(len(data[i])):
        if j == 0:
            data[i][j] = data[i-1][j] + data[i][j]
        elif j == (len(data[i]) - 1):
            data[i][j] = data[i-1][len(data[i])-2] + data[i][j]
        else:
            data[i][j] = max(data[i-1][j-1] + data[i][j], data[i-1][j] + data[i][j])

answer = max(data[n-1])
print(answer)
