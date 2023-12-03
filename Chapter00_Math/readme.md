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
