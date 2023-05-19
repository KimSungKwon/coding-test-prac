
# 정렬

- 파이썬의 정렬 함수: O(*NlogN*)  => 왠만하면 걍 **내장 함수** 쓰자 or **계수정렬**
## sort
- iterable.**sort**(reverse=False): iterable의 데이터를 정렬
- iterable.sort(**key = lambda** x: (-x[1], x[2], -x[0]))	// 2번째 내림차순 -> 3번째 오름차순 -> 1번째 내림차순

### merge sort
직접 구현해야 할 때.. 이거 쓰기
	
    # 리스트의 길이가 1이 될 때 까지 분할
	def merge_sort(unsorted_list):
	    if len(unsorted_list) <= 1:
	        return unsorted_list

	    # 리스트를 2개로 분할
	    mid = len(unsorted_list) // 2
	    
	    left = unsorted_list[ :mid]
	    right = unsorted_list[mid: ]

	    # 분할한 리스트를 각각 merge_sort 진행
	    _left = merge_sort(left)
	    _right = merge_sort(right)

	    return merge(_left, _right)

	# 1로 쪼개진 리스트들을 병합
	def merge(left, right):
	    i, j = 0, 0
	    sorted_list = []
	    # 맨 앞 두개끼리 비교해서 배열에 넣기
	    while i < len(left) and j < len(right):
	        if left[i] < right[j]:
	            sorted_list.append(left[i])
	            i += 1
	        else:
	            sorted_list.append(right[j])
	            j += 1

	    # 나머지들 다 넣기
	    while i < len(left):
	        sorted_list.append(left[i])
	        i += 1
	    while j < len(right):
	        sorted_list.append(right[j])
	        j += 1
	        
	    return sorted_list

	unsorted_list = list(map(int, input().split()))
	print(merge_sort(unsorted_list))

### 튜플의 정렬
튜플이 3개의 원소로 구성되있다면 
첫 번째 원소의 순서에 맞게 정렬 -> 두 번째 원소의 순서에 맞게 정렬 -> 세 번째 원소의 순서에 맞게 정렬

    a = [(5, 1, 5), (3, 5, 5), (3, 1, 9), (3, 1, 1)]
    a.sort
    
    => [(3, 1, 1), (3, 1, 9), (3, 5, 5), (5, 1, 5)]

## 기타 정렬 알고리즘들
- 선택 정렬:  O(*N²*)
> 아이디어가 간단
- 삽입 정렬: O(*N²*) 
> 데이터가 정렬되어 있을 때 가장 빠름
> 앞에서부터 하나씩 확인해서 적절한 위치에 삽입
- 퀵 정렬: O(*NlogN*)
> 보편적임 
> 기준(피벗)데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈
- 계수 정렬: O(*N + K*)
> 데이터의 크기가 한정된 경우에만. 매우 빠름
> 특정한 값을 가지는 데이터의 개수를 카운트
