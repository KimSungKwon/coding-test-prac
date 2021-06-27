n, m, k = map(int, input().split())  # m: 덧셈횟수 k: 연속 횟수 
data = list(map(int, input().split()))
data.sort(reverse=True)

first = data[0]   # 배열 내 가장 큰 수
second = data[1]  # 배열 내 두번 째로 큰 수
result = 0

while m > 0:      # first를 k번 더하고 second를 1번 더함 
  for i in range(k):
    result += first
    m -= 1
    if m == 0:
      break
  result += second
  m -= 1

print(result)
