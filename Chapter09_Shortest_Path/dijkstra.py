import sys
input = sys.stdin.readline
INF = 987654312

n, m = map(int, input().split())
start = int(input())    # 시작 노드 입력

# 노드들의 번호가 1번부터 시작하려고 n+1
graph =[[] for i in range(n+1)] # 인접 노드 그래프
visited = [False] * (n+1)       # 방문 여부 
distance = [INF] * (n+1)        # 최단거리 테이블

# 그래프 값 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))     # 노드a에서 b로 가는 거리는 c

# 최단거리 테이블에서 가장 작은 값 노드 가져오기
def get_shortest_node():
    min_value = INF
    index = 0   # 가장 짧은 최단거리 노드의 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    # 시작노드의 인접노드들 최단거리 테이블 초기화
    for nodes in graph[start]:
        distance[nodes[0]] = nodes[1]
    # 테이블에서 가장 낮은 값을 가진 노드를 방문
    for i in range(1, n+1):
        now = get_shortest_node()
        visited[now] = True
        # 방금 방문한 노드의 인접노드와의 거리를 비교해서 테이블 갱신
        for nodes in graph[now]:
            cost = distance[now] + nodes[1]
            if cost < distance[nodes[0]]:
                distance[nodes[0]] = cost

dijkstra(start) # 알고리즘 실행

# 모든 노드로 가기 위한 거리 출력
for i in range(n+1):
    if distance(i) == INF:
        print("INF")
    else:
        print(distance[i])
