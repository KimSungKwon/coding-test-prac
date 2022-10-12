# 최단 경로
## 다익스트라 vs 플로이드 워셜

| 이름 | 시간 복잡도 | 구현 난이도 | 역할 |
|--|--|--|--|
| 다익스트라 | O(ElogV) | 어려움 | **한 지점에서** 다른 모든 지점까지의 최단경로 계산 |
| 플로이드 워셜 | O(V³) | 쉬움 | **모든 지점에서** 다른 모든 지점까지의 최단경로 계산 |

## 다익스트라
**우선순위 큐** 사용: 자동으로 '최단거리 값'이 가장 짧은 노드를 pop하게
> 1. 출발 노드 설정
> 2. 최단 거리 테이블 초기화 (출발 노드를 제외한 모든 노드의 최단 거리=INF)
> 3. 출발 노드를 큐에 삽입 (최단 거리=0)
> 4. 우선순위 큐 pop
> 4.1 pop한 노드가 이미 처리된거면 무시. (우선순위 큐의 거리 정보 > 테이블의 거리 정보) 
> 5. 해당 노드를 거쳐 다른 노드로 가는(연결된) 비용을 계산하여 테이블 갱신
> 5.1 갱신된 노드들은 우선순위 큐에 삽입
> 6. iv 와 v 반복

    import heapq
	
	graph = [[] for _ in range(v + 1)]
	distance = [INF] * (v + 1)	# 2

	for _ in range(e):
		graph[a].append(b, c)	# a노드에서 b노드로 가는 비용 = c

	def dijkstra(start):
		heapq.heappush(q, (0, start))
		distance[start] = 0		# 3
	
		while q:
			dist, now = heapq.heappop(q)	# 4
			if distance[now] < dist:
				continue	# 4.1
			# 5
			for data in graph[now]:	# graph[now] = [(노드b, 거리c), ...]
				cost = dist + data[1]
				if cost < distance[data[0]]:
					distance[data[0]] = cost
					heapq.heappush(q, (cost, data[0]))	# 5.1

	dijkstra(start)

## 플로이드 워셜
**다이나믹 프로그래밍** 사용: '**거쳐가는 노드(k)**'를 기준으로 최단 거리 테이블을 갱신(완전탐색)
> 점화식: Dab = min(Dab, Dak + Dkb) 

    graph = [[INF] * (v + 1) for _ in range(v + 1)]
	for _ in range(e):
		graph[a][b] = c	# a에서 b로 가는 비용 = c

	# floyd 
	for k in range(1, v + 1):
		for a in range(1, v + 1):
			for b in range(1, v + 1):
				graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])