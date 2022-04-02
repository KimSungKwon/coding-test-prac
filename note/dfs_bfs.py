'''
DFS
'''
graph = [[~], [~], ... [~]] # 각 노드가 연결된 정보를 2차원 리스트로 표현
visited = [False] * 9 # 각 노드의 방문여부 

def dfs(graph, v, visited):
  # 현재 노드(v)를 방문처리
  visited[v] = True
  print(v, end=' ')
  
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in range(graph[v]):
    if not visited[i]:
      dfs(graph, i, visited)
      
dfs(graph, 1, visited)
      
'''
BFS
'''
from collections import deque

graph = [[~], [~], ... [~]] # 각 노드가 연결된 정보를 2차원 리스트로 표현
visited = [False] * 9 # 각 노드의 방문여부

def bfs(graph, start, visited):
  # Queue 사용
  q = deque([start])
  visited[start] = True  # 현재 노드 방문 처리
  
  # 큐가 빌 때까지 반복
  while q:
    # pop
    v = q.popleft()
    print(v, end=' ')
    
    # 해당 원소(v)와 연결된, 아직 방문하지 않은 노드들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        
bfs(graph, 1, visited)
