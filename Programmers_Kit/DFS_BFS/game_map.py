'''
게임 맵 최단거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3

'''

from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    # bfs 1. 시작 노드 삽입
    q = deque()
    q.append((0, 0))
  
    # bfs 2. 큐가 빌 때 까지 bfs
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 제외해야 하는 노드인지 판별
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 제외해야 하는 노드가 아니면 큐에 삽입 
            if maps[nx][ny] != 0 and maps[nx][ny] == 1:
                # 노드 값 업데이트(해당 노드까지 가는데 필요한 걸음 수) 후 삽입
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                
    answer = maps[n - 1][m - 1]
    
    # 
    if answer == 1 or answer == 0:
        answer = -1
        
    return answer
