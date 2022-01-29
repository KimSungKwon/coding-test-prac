INF = 987654321
n =  int(input())
m = int(input())

# n+1: 노드 번호가 1부터 시작하게
graph = [[INF] * (n+1) for _ in range(n+1)]

# i번에서 i번 노드로 가는 경로는 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# a에서 출발, b에 도착하는 경로 길이 = c
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 알고리즘. a에서 b로 바로 가는 거리 vs k 거쳐서 가는 거리
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 업데이트된 테이블 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
