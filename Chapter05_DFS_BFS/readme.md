# 탐색 알고리즘 DFS / BFS

## DFS
스택 활용. 스택에 삽입된 순서가 탐색 순서
> 1. 탐색 시작 노드를 **스택에 삽입, 방문 처리**
> 2. 스택의 top 노드 (pop하면 나오는)와 연결된 방문 안 한 노드가 있으면 그 노드를 **스택에 삽입, 방문 처리**
> 2-1 .  방문하지않은 인접노드가 없으면 top 노드를 pop
>  3.  2번 반복

    def dfs(graph, v, visited):
	    visited[v] = True	// 1
	    for i in graph[v]:	// 2
		    if not visited[i]:
			    // 변형 가능
			    dfs(graph, i, visited)	// 3

## BFS
큐 활용. 큐에 삽입된 순서가 탐색 순서
> 1. 탐색 시작 노드를 **큐에 삽입, 방문처리**
> 2. 큐에서 노드를 꺼내 해당 노드의 [인접, 방문X] 노드를 모두 **큐에 삽입, 방문처리**
> 3. 2번 반복

    def bfs(graph, start, visited):
	    q = deque()
	    q.append(start), visited[start] = True	// 1
	    while q:
		    v = q.popleft()
		    for i in graph[v]:	// 2
			    // 변형 가능
			    if not visited[i]:
				    q.append(i), visited[i] = True