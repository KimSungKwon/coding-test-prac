
# 수학
## 소수 리스트 구하기
```python
# 에라토스테네스의 채
arr = [True]*(N+1)
arr[0] = False
arr[1] = False	# 1은 소수가 아니다

for i in range(2, int(math.sqrt(N))+1):	# sqrt: 제곱근(루트)
    if arr[i]:	# 아직 소수인지 판명이 안 났으면
        for mul in range(i*2, N+1, i):	# if i==5: 10, 15, 20 ...
            arr[mul] = False

prime_list = []
for i in range(2, N+1):
	if arr[i]: prime_list.append(i)
```
## 소인수 분해

```python
n = int(input())		# n: 분해할 값

for i in range(2, n+1):		# i 값으로 분해
    if (i * i > n):		# 최적화
        break
    while (n % i == 0):		# i 값으로 분해가 가능하면
        n = n / i 
        print(i)

if n != 1: print(int(n))	# 1은 소수가 아니므로
```
