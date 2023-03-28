# 그래프 이론
## 서로소 집합 연산
union & find_parent : **무방향** 그래프의 사이클 판별 가능
> find_parent의 값이 서로 다르면? union 해서 합침
> find_parent의 값이 같으면? cycle 있음

    # parent 테이블 초기화
    for i in range(1, v + 1):
	    parent[i] = i
	    
    def find_parent(parent, x):
	    if parent[x] != x:	# 루트 노드가 아니면, 루트 노드를 찾을 때 까지 재귀
		    parent[x] = find_parent(parent, parent[x])
	    return parent[x]

    def union(parent, a, b):
	    # 서로 부모를 찾아서
	    a = find_parent(parent, a)
	    b = find_parent(parent, b)
		
	    # 더 적은 번호의 노드로 통합
	    if a < b:
		    parent[b] = a
	    else:
		    parent[a] = b

    if find_parent(parent, x) == find_parent(parent, y): cycle = True 

## 최소 신장 트리 *Minimum Spanning Tree*
- 모든 노드를 방문할 수 있고 사이클이 없는 그래프 (== 트리)
- 최소한의 비용으로 **신장 트리를 찾거나 만들 때** 씀
(가장 적은 비용으로 모든 노드를 연결) = 그리디 알고리즘
-  방향X, 사이클X

- 도로를 추가해 모든 섬을 연결하는 문제 등에 활용

### 크루스칼 알고리즘
union & find_parent 함수 사용
> 1. edge들을 비용에 따라 오름차순으로 정렬
> 2. edge를 하나씩 확인하여 신장 트리에 포함시킴 
> 2-1. 사이클 발생?(=부모가 같은가?) 최소 신장 트리에 포함X
> 3. 모든 edge들에 대해 2번의 과정 실행

    for _ in range(e):
	    edges.append( (cost, a, b) )
	edges.sort()	# 1

	for edge in edges:	# 2
		cost, a, b = edge
		if find_parent(parent, a) != find_parent(parent, b):	# 2-1
			union(parent, a, b)	
			result += cost
### 프림 알고리즘
우선순위 큐 (min heap) 사용 = cost 순으로
MST 등록 여부 배열 사용
> 1. 시작 노드를 min heap에 삽입 (시작노드라서 cost = 0)
> 2. min heap을 pop하고, 그 노드가 MST에 등록됐는지 확인
> 3. 등록 안 됐으면 등록 한 후 cost 추가. 등록 되어있으면 스킵 
> 4.  pop한 노드와 연결돼있고 아직 등록돼있지 않은 노드를 min heap에 삽입
> 5. heap이 빌 때 까지 2번부터 반복 

    for _ in range(e):
	    graph[a].append( (c, b) )
	    graph[b].append( (c, a) )
	
	heapq.heappush(min_heap, (0, 1)   # 1

	while min_heap:   # 5
		cost, now = heapq.heappop(min_heap)   # 2, 3
		if not visited[now]: visited[now] = True, answer += cost

		for c, v in graph[now]:   # 4
			if not visited[v]: heapq.heappush(min_heap, (c, v))
    
	
## 위상 정렬 *topology sort*
- **방향** 그래프의 모든 노드를 **방향성에 거스르지 않도록 순서대로 나열** 
*(ex. 커리큘럼 선수과목)* 
> 1. 진입차수가 0인 노드를 큐에 삽입
> 2. 큐가 빌 때까지 노드를 한 개씩 꺼내 해당 노드에서 출발하는 간선을  그래프에서 제거 (진입차수 - 1)
> 3. 새롭게 진입차수가 0이된 노드를 큐에 삽입
> 4. 큐에서 빠져나간 노드 순으로 출력

	indegree = [0] * (v + 1)
	graph = [[] for _ in range(v + 1)]
	
	for _ in range(e):
	    graph[a].append(b)	# 방향 그래프라서
	    indegree[b] += 1

    def topology_sort():
	    q = deque()
	    
	    for i in range(1, v + 1):	# 1
	    	if indegree[i] == 0:
		    q.append(i)
	
	    while q:	# 2
	        now = q.popleft()
		result.append(now)
			
		for i in graph[now]:
		    indegree[i] -= 1
		    if indegree[i] == 0:	# 3
		        q.append(i)
