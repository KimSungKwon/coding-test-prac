'''
단어 변환
https://programmers.co.kr/learn/courses/30/lessons/43163

BFS. 
'''
from collections import deque


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    n = len(words)
    # 각 단어는 한번 밖에 못 쓰므로 방문 체크
    visited = [False] * n
    
    # bfs 1.  시작 노드 삽입
    q = deque()
    q.append([begin, 0])

    while q:
        top = q.popleft()
        
        # goal : pop한 노드가 목표 단어이면
        if top[0] == target:
            return top[1]

        # bfs 2.  pop한 노드에서 방문할 수 있는 모든 인접 노드를 검사(이미 방문 했는지, 단어가 한 개만 다른지)하고 삽입
        for i in range(n):
            temp = words[i]
            diff = 0
            
            # 2-1. 이미 방문 했는지 
            if visited[i] == True:
                continue
            
            # 2-2. 단어가 한 개만 다른지 검사
            for j in range(len(begin)):
                if top[0][j] != temp[j]:
                    diff += 1
                    
            # 2-3. 모든 검사를 통과하면 삽입
            if diff < 2:
                q.append([temp, top[1] + 1])
                visited[i] = True
                # print(top[0] + " -> " + temp)
        

    return 0
