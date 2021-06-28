n, m = map(int, input().split())

result = 0
for i in range(n):
  data = list(map(int, input().split()))
  lowest = min(data)  # 행의 최소값 
  if (lowest > result):
    result = lowest   # 행의 최소값들 중 가장 큰 값

print(result)
