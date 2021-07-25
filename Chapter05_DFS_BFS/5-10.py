n, m = map(int, input().split())
graph = []
result = 0

# 그래프 초기화
for i in range(n):
    graph.append(list(map(int, input())))

# graph[x][y]가 0이면 (아직 방문 안 했으면) dfs 돌리고 True.  1이면(방문했거나 칸막이) False.
def dfs(x, y):
    # 그래프에서 벗어나면
    if x < 0 or y < 0 or x >= n or y >= m:
            return False
    # 방문 안 했으면
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
        return True
    return False

# 모든 경우의 수에 dfs 돌림
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
