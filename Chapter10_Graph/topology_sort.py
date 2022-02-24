from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v+1) # 노드번호는 1번부터 시작
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # a에서 b로 방향간선
    indegree[b] += 1    # b의 진입차수 증가

def topology_sort():
    result = []
    q = deque()    # 진입차수가 0인 노드만 삽입 되는 큐

    # 처음에 진입차수가 0인 노드들을 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:    # 큐가 빌 때까지
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1    # now에서 진입할 수 있는 노드들 진입차수 -1
            if indegree[i] == 0:
                q.append(i)    # 새로 진입차수가 0되면 큐에 삽입
    
    # 정렬결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()
