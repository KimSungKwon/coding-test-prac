"""
Q31 금광

바텀업 순서가 열(column)부터 이므로 2중 for문에서 i, j 순서 주의
"""

t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    dp = []
    index = 0
    for k in range(n):
        dp.append(data[index : index + m])
        index += m
    
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j-1] + dp[i][j], dp[i+1][j-1] + dp[i][j])
            elif i == (n - 1):
                dp[i][j] = max(dp[i-1][j-1] + dp[i][j], dp[i][j-1] + dp[i][j])
            else:
                dp[i][j] = max(dp[i-1][j-1]+ dp[i][j], dp[i][j-1] + dp[i][j], dp[i+1][j-1] + dp[i][j])

    answer = 0
    for i in range(n):
        answer = max(answer, dp[i][m - 1])

    print(answer)
