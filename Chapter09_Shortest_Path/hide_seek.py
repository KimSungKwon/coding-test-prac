"""
Q40 숨바꼭질
"""

import heapq
INF = 987654321

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

q = []
heapq.heappush(q, (0, 1))    # (0, 1)
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)    # (dist, now)
    # dist *= -1
    
    if dist > distance[now]:
        continue

    for node in graph[now]:    #(num, dist)
        cost = dist + node[1]

        if cost < distance[node[0]]:
            distance[node[0]] = cost
            heapq.heappush(q, (cost, node[0]))

idx = 0
maxV = max(distance[1:])
num = 0
for i in range(1, n + 1):
    if distance[i] == maxV:
        idx = i
        break
for i in range(1, n + 1):
    if distance[idx] == distance[i]:
        num += 1

print(idx, maxV, num)
