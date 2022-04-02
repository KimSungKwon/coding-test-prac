'''
특정 거리의 도시 찾기
p.339

모든 간선의 비용이 동일할 때는 BFS를 이용하여 최단거리 구함
'''
from collections import deque

n, m, k, x = map(int, input().split())    # user input
graph = [[] for _ in range(n+1)] 
visited = [False] * (n+1)    
result = []    # inputs nodes that distance == k

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, v, visited):
    dist = 0
    q = deque()
    q.append((v, 0))    # (nodeId, distance)
    visited[v] = True
    
    while q:
        curr, dist = q.popleft()
        
        for i in graph[curr]:
            if not visited[i]:
                q.append((i, dist+1))
                visited[i] = True
                if (dist+1) == k:
                    result.append(i)
            
bfs(graph, x, visited)

print(result)
