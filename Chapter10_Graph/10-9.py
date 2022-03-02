'''
나중에 다시 풀기
'''

from collections import deque

v = int(input())

indegree = [0] * (v+1)
time = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for i in range(v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    
    # 순서 거꾸로. a->b 가 아니라 b->a
    for j in range(1, len(data)-1):
        graph[data[j]].append(i)

def topology():
    q = deque()
    result = []
    
    for i in range(v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append[i]
