# 최단 경로
## heap과 priority queue (& Binary Search Tree)
 1. heap: 우선순위 큐를 구현하기 위한 자료구조 (Binary Search Tree)
 2. priority queue: 우선순위가 가장 높은 데이터를 먼저 pop 
>heapq 사용

    import heapq
    q = []
    heapq.heapify(q)	# q를 heap으로 만듬 (필수 아닌거같음 => 자동 정렬을 위해)
    heapq.heappush(q, (2, node1))	# q에 (2, node1)삽입. 우선순위 값은 2
    heapq.heappush(q, (0, node2))	# q에 (0, node2)삽입. 우선순위 값은 0	(자동으로 정렬됨)
    heapq.heappop(q)	# pop.. (0, node2)

 

## 다익스트라 vs 플로이드 워셜

| 이름 | 시간 복잡도 | 구현 난이도 | 역할 |
|--|--|--|--|
| 다익스트라 | O(ElogV) | 어려움 | **한 지점에서** 다른 모든 지점까지의 최단경로 계산 |
| 플로이드 워셜 | O(V³) | 쉬움 | **모든 지점에서** 다른 모든 지점까지의 최단경로 계산 |

## 다익스트라
**우선순위 큐(priority queue : heapq)** 사용: 자동으로 '최단거리 값'이 가장 짧은 노드를 pop하게
> 1. 출발 노드 설정
> 2. 최단 거리 테이블 초기화 (출발 노드를 제외한 모든 노드의 최단 거리=INF)
> 3. 출발 노드를 큐에 삽입 (최단 거리=0)
> 4. 우선순위 큐 pop 
>> 4-1. pop한 노드가 이미 처리된거면 무시. (우선순위 큐의 거리 정보 > 테이블의 거리 정보) 
> 5. 해당 노드를 거쳐 다른 노드로 가는(연결된) 비용을 계산하여 테이블 갱신
>> 5.1. 갱신된 노드들은 우선순위 큐에 삽입
> 6. 4와 5 반복

    import heapq
	
	graph = [[] for _ in range(v + 1)]
	distance = [INF] * (v + 1)	# 2

	for _ in range(e):
		graph[a].append((b, c))	# a노드에서 b노드로 가는 비용 = c

	def dijkstra(start):
		heapq.heappush(q, (0, start))   # 3
		distance[start] = 0	
	
		while min_heap:
			dist, now = heapq.heappop(min_heap)	# 4
			if distance[now] < dist:
				continue	# 4.1
			# 5
			for data in graph[now]:	# graph[now] = [(노드b, 거리c), ...]
				cost = dist + data[1]
				if cost < distance[data[0]]:
					distance[data[0]] = cost
					heapq.heappush(min_heap, (cost, data[0]))	# 5.1

	dijkstra(start)

## 플로이드 워셜
**다이나믹 프로그래밍** 사용: '**거쳐가는 노드(k)**'를 기준으로 최단 거리 테이블을 갱신(완전탐색)
> 그래프 문제인가? -> 정점의 수가 1000개 이하인가? -> 모든 정점들 간의 최단거리를 구하면 편한가? -> 플로이드 워셜
>
> 점화식: D[a][b] = min(D[a][b], D[a][k] + D[k][b]) 

    graph = [[INF] * (v + 1) for _ in range(v + 1)]
    
    # 자신->자신 : 0으로 채우기
    for a in range(1, n + 1):
		for b in range(1, n + 1):
			if a == b: graph[a][b] = 0
	
	# 초기 입력 받기
	for _ in range(e):
		graph[a][b] = c	 # a에서 b로 가는 비용 = c

	# floyd .. 1부터 k까지를 중간경로로 해서 a->b 계산
	for k in range(1, v + 1):
		for a in range(1, v + 1):
			for b in range(1, v + 1):
				graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
	
	# 출력
	for a i range(1, v + 1):
		for b in range(1, v + 1):
			if graph[a][b] != INF:
				print(graph[a][b], end=' ')
		print()
