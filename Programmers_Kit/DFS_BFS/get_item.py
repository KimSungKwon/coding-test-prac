'''
아이템 줍기
https://school.programmers.co.kr/learn/courses/30/lessons/87694#

한 칸 단위로 하면 ㄷ이 ㅁ과 같이 취급될 수 있으므로 두 칸 단위로  만듬

테스트 케이스 15, 20 안 됨
'''

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    itemX *= 2    # 두 칸 단위로
    itemY *= 2
    characterX *= 2
    characterY *= 2
    matrix = [[2] * (102) for _ in range(102)]    # 1이상 50이하 => 좌표계엔 51칸 => 51 * 2

    # 좌표계에 점찍기
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rec)    # 두 칸 단위로
        
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    matrix[i][j] = 0
                elif matrix[i][j] != 0:
                    matrix[i][j] = 1

    # 4방향 탐색하는 bfs 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((characterX, characterY))

    while q:
        now = q.popleft()
        
        if now == (itemX, itemY):
            return matrix[now[0]][now[1]] // 2    # 두 칸 단위를 다시 한 칸으로

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if nx < 0 or nx >= 100 or ny < 0 and ny >= 100:
                continue
            # 1인 부분(한 번도 안 간 길)만 따라가기 
            if matrix[nx][ny] == 1:
                q.append((nx, ny))
                matrix[nx][ny] += matrix[now[0]][now[1]]
            
    return answer
