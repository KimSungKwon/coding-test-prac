"""
입력범위가 매우 좁음 (1~100)
따라서 플로이드 알고리즘 사용
"""

INF = 987654321
n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

# a에서 a로 이동하는 거리: 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 방향X 그래프. 거리는 무조건 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

# 1~k~x의 최단거리: 1~k + k~x
answer = graph[1][k] + graph[k][x]
if answer >= INF:
    answer = -1
    
print(answer)
