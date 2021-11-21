"""
게임 개발
"""

def solution(m, pos, M):
    mapp = [[0] * m[0] for _ in range(m[1])]
    mapp[pos[0]][pos[1]] = 1
    # 북 동 남 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def turn_left():
        pos[2] -= 1
        if pos[2] == -1:
            pos[2] = 3
    
    count = 1
    failed = 0
    while (1):
        turn_left()
        nx = pos[0] + dx[pos[2]]
        ny = pos[1] + dy[pos[2]]
        if mapp[nx][ny] == 0 and M[nx][ny] == 0:
            mapp[nx][ny] = 1
            count += 1
            pos[0] = nx
            pos[1] = ny
            failed = 0
            continue
        else:
            failed += 1 
        if failed == 4:
            nx = pos[0] - dx[pos[2]]
            ny = pos[1] - dy[pos[2]]
            if M[nx][ny] == 0:
                pos[0] = nx
                pos[1] = ny
            else:
                break
            failed = 0

    return count

print(solution( [4, 4], [1, 1, 0], [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]  ))
