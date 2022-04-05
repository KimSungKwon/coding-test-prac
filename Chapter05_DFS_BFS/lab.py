'''
Q 16 연구소

다시 풀기
'''

from collections import deque

n, m = map(int, input().split())
data = []    # 원본 지도
temp = [[0] * m for _ in range(n)]    # 새로 벽을 설치 한 지도

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# bfs로 바이러스 퍼트리기
def virus(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))

# 완전탐색으로 0의 개수 구하기
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    
    return score

# dfs로 모든 경우의 수로 벽 설치해서 바이러스 퍼트리고 0의 개수의 최대값 구하기
def dfs(count):
    global result
    
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)

print(result)
