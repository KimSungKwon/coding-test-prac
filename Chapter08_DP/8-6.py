'''
개미 전사
dp[i]: 0 ~ i 까지의 창고 중에서 가장 많이 훔칠 수 있는 값
연속된 번호의 창고를 연달아 훔칠 수 없으므로  dp[i-1]까지의 값과 dp[i-2]+ i번 창고의 값을 비교하여 더 높은걸 선택
dp[i] = max( dp[i-1], dp[i-2]+arr[i] )
'''

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * 100

dp[0] = arr[0]
dp[1] = arr[1]

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])

print(dp[n-1])
