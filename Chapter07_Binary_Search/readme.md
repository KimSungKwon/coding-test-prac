# 이진 탐색

## 이진 탐색

 - **정렬되어 있어야만** 사용 가능
 - 위치를 나타내는 변수 **시작점, 중간점, 끝점**을 사용

 > 반복문으로 구현한 이진탐색

    def binary(arr, target, start, end):
	    while start <= end:
		    mid = (start + end) // 2
	
			if arr[mid] == target:
				return mid
			elif arr[mid] > target:
				end = mid - 1
			else:
				start = mid + 1
				
		return None
    
### 파라메트릭 서치
**원하는 조건을 만족하는 가장 알맞은 값** 을 찾는 문제 
> ex) 범위 내에서 조건을 만족하는 가장 큰 값을 찾는다면, 

> start: 최소값, end: 최대값, mid: 조건에 맞는 값(?) 즉, start와 end도 mid(타겟값)에 어울리는 값으로 설정해야함

		    ...
    while start <= end:
	    mid = (start + end) // 2
	    
	    # 조건값(total) 계산
	    for i in range(n):
		temp = arr[i] - mid
		if temp > 0:
			total += temp
			
	    if total == target:
	        return mid
	    elif total >= target:
		start = mid + 1
	    else
			...
## 내장 라이브러리
### bisect
**정렬된 리스트**에서 **값이 특정 범위에 속하는 원소의 개수**를 구할 때 효과적 

    from bisect import bisect_left, bisect_right
    
    data = [1, 2, 4, 4, 8]
    
    # 정렬된 순서를 유지하며 리스트 a에 데이터 x를 삽입할 가장 왼/오른쪽 인덱스를 찾음
    bisect_left(data, x) 	# return 2
    bisect_right(data, x)	# return 4
    
    # 값이 [lh, rh]에 속하는 데이터의 개수 
    num = bisect(data, rh) - bisect(data, lh)
