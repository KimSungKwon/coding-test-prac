"""
Q17 경쟁적 전염
"""

from collections import deque

n, k = map(int, input().split())
graph = []
virus = []
time = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    graph.append(list(map(int, input().split())))

# 바이러스들의 정보를 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j, 0))

# 번호가 낮은 바이러스를 앞쪽에 (번호가 낮을수록 우선권)
virus.sort()

s, t_x, t_y = map(int, input().split())

# bfs
q = deque(virus) # 큐에 여러개를 한번에 넣으면 한번에 여러 좌표에서(?) bfs 가능

while q:
    v, x, y, t = q.popleft()

    if t >= s:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                q.append((v, nx, ny, t + 1))

print(graph[t_x - 1][t_y - 1])
