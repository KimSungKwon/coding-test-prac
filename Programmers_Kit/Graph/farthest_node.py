"""
가장 먼 노드
https://school.programmers.co.kr/learn/courses/30/lessons/49189

위상정렬 이용
"""
from collections import deque

def solution(n, edge):
    answer = 0
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    q = deque()
    q.append(1)
    indegree[1] = 1
    
    while q:
        now = q.popleft()
        for e in graph[now]:
            if indegree[e] == 0:
                indegree[e] = indegree[now] + 1
                q.append(e)
                
    max_degree = max(indegree)
    for i in range(n + 1):
        if indegree[i] == max_degree:
            answer += 1
    
    return answer
