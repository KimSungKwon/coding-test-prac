'''
최단 거리 값을 가지는 노드를 고를 때 리스트 대신 heap(우선순위 큐) 사용 : (최단거리, 노드번호)
우선순위 큐에는 최단거리 테이블이 갱신된 노드만 삽입됨
방문여부 판단은 따로 리스트로 관리 안하고, 우선순위 큐에서 pop된 최단거리 값이, 테이블 값보다 크면 이미 방문된 걸로 판단
'''

import sys
import heapq
input = sys.stdin.readline
INF = 987654312

n, m = map(int, input().split())
start = int(input())    # 시작 노드 입력

# 노드들의 번호가 1번부터 시작하려고 n+1
graph =[[] for i in range(n+1)] # 인접 노드 그래프
distance = [INF] * (n+1)        # 최단거리 테이블

# 그래프 값 입력
for _ in range(n+1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))     # 노드a에서 b로 가는 거리는 c


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    # 큐가 다 빌 때 까지
    while q:
        dist, now = heapq.heappop()
        # 방문 여부 판단
        if dist > distance[now]:
            continue
        # 방금 방문한 노드의 인접노드와의 거리를 비교해서 테이블 갱신
        for nodes in graph[now]:
            cost = dist + nodes[1] 
            if cost < distance[nodes[0]]:
                distance[nodes[0]] = cost
                # 테이블 갱신했으므로 heap에 삽입
                heapq.heappush(q, (cost, nodes[0]))
                
dijkstra(start) # 알고리즘 실행

# 모든 노드로 가기 위한 거리 출력
for i in range(n+1):
    if distance(i) == INF:
        print("INF")
    else:
        print(distance[i])
