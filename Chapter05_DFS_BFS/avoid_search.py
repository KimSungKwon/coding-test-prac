"""
Q20 감시 피하기

흩뿌리기 방법으로 장애물 설치, dfs로 search 함수 구현하려 했으나 실패 => 교재의 brute force는 성공
"""

n = int(input())
graph = []
temp = [['X'] * (n) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(input().split()))


result = False

"""
# 실패 
def search(x, y, d):
    global result
    nx = x + dx[d]
    ny = y + dy[d]
    
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
        if temp[nx][ny] == 'S':
            return True
        if temp[nx][ny] == 'O':
            return result
            
        search(nx, ny, d)

    return result
"""
# 성공(교재)
def search(x, y, d):
    if d == 0:
        while x >= 0:
            if temp[x][y] == 'S':
                return True
            if temp[x][y] == 'O':
                return False
            x -= 1
    if d == 1:
        while y < n:
            if temp[x][y] == 'S':
                return True
            if temp[x][y] == 'O':
                return False
            y += 1
    if d == 2:
        while x < n:
            if temp[x][y] == 'S':
                return True
            if temp[x][y] == 'O':
                return False
            x += 1
    if d == 3:
        while y >= 0:
            if temp[x][y] == 'S':
                return True
            if temp[x][y] == 'O':
                return False
            y -= 1

answer = False
def dfs(count):
    global answer
    safe = True
    if count == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j] = graph[i][j]

        for i in range(n):
            for j in range(n):
                if temp[i][j] == 'T':
                    for k in range(4):
                        if search(i, j, k):
                            safe = False

        if safe:
            answer = True
            
        return                
        
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                count += 1
                graph[i][j] = 'O'
                
                dfs(count)
                
                count -= 1
                graph[i][j] = 'X'


dfs(0)

if answer:
    print("YES")
else:
    print("NO")
