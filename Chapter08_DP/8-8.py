'''
효율적인 화폐 구성

greedy와 다르게 화폐 단위가 배수가 아님
작은 화폐부터 차례대로 dp 채우기

N원을 만들기 위해 필요한 최소 개수는
이전 화폐들로만 만들었던 필요 개수와 새로운 화폐를 추가해 만든 필요 개수를 비교

dp[N] = min(dp[N], dp[N-money]+1) # money는 화폐 단위
'''

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

INF = 987654321
dp = [INF] * 1000001
dp[0] = 0

# money: 화폐 가치
for money in arr:
    for i in range(money, m+1):
        dp[i] = min(dp[i], dp[i-money]+1)

print(dp[m])
