from collections import deque

def solution(n, m, graph):
    queue = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # start at [0, 0]
    queue.append((0, 0))
    
    while queue:
        # bfs  1. pop
        x, y = queue.popleft()
        
        # bfs  2. push near nodes
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # bfs  3. check success or fail 
            
            # fail condition : position is out of grapgh
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # fail condition : position is wall
            if graph[nx][ny] == 0:
                continue
            
            # success condition : first approach
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


    return graph[n-1][m-1]

print(solution( 3, 3, [ [1,1,0], [0,1,0], [0,1,1] ]  ))
