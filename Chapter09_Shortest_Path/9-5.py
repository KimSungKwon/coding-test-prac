'''
입력값의 범위가 매우 커서 힙 쓰는 다익스트라로
'''

import heapq

INF = 987654321
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# 힙 쓰는 다익스트라
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        
        for nodes in graph[now]:
            cost = dist + nodes[1]
            
            if cost < distance[nodes[0]]:
                distance[nodes[0]] = cost
                heapq.heappush(q, (cost, nodes[0]))

dijkstra(c)

count= 0        # 갈 수 있는 도시의 수
maximum = 0     # 총 걸리는 시간 == 가장 오래 걸린 시간

for i in range(len(distance)):
    if distance[i] != INF:
        count += 1
        maximum = max(maximum, distance[i])

print(count-1, maximum) # count-1: 자기 자신은 미포함
