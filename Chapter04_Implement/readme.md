# 구현

## 구현에 쓰이는 기술들
### **좌표 이동**
	시계 방향 이동 (U, R, D, L)
	
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    nx = x + dx[i],  ny = y + dy[i]

### **방향 회전**
	
    turn_left(): 
	    global direction
	    direction -= 1
	    if direction == -1: 
		    direction = 3
	       ...
	nx = x + dx[direction] ...

## 완전탐색
모든 경우의 수를 빠짐없이 다 계산.
- 일반적으로 DFS / BFS 이용하여 해결

## 시뮬레이션
문제에서 요구하는 복잡한 논리나 동작과정을 잘 구현
- 원소를 나열하는 모든 경우의 수를 고려: 순열 / 조합 라이브러리 사용
> itertools 라이브러리 사용

    from itertools import permutations	// 순열: 순서 다르면 다른거 취급
    from itertools import combinations	// 조합: 순서 달라도 같은거 취급
    from itertools import product	// 중복순열: 순열 + 원소의 중복사용 허용
    from itertools improt combinations_with_replacement	// 조합 + 중복허용
    
    data = ['A', 'B', 'C']
    
    permut = list(permutations(data, 3))	// 데이터 중 3개를 뽑아 나열 (순열)
	combi = list(combinations(data, 2))	// 데이터 중 2개를 뽑아 나열 (조합)
	prod = list(product(data, repeat=2))	// 데이터 중 2개를 뽑아 나열 (중복순열)
	combi_rpt = list(combinations_with_replacement(data, 2)) // 데이터 중 2개를 뽑아..
