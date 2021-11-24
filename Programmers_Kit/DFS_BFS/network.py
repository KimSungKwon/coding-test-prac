'''
네트워크
https://programmers.co.kr/learn/courses/30/lessons/43162

bfs로 풀이. 모든 경우의 수를 구해야 하기 떄문에 for문으로 bfs 실행
'''
from collections import deque
def solution(n, computers):
    answer = 0
   
    q = deque()
    visited = [False] * n
    
    def bfs(v):
        #bfs 1.  시작 노드 삽입
        q.append(v)
        
        #bfs 2.  연결된 모든 노드를 방문할 때 까지 반복
        while q:
            temp = q.popleft()
            # 방문한 노드(temp) 방문처리
            visited[temp] = True
            # 방문하지 않은(visited[i]==False) 연결된(computers[temp][i]==1) 모든 노드 방문
            for i in range(n):
                if computers[temp][i] == 1 and visited[i] == False:
                    q.append(i)
   
    for a in range(n):
        if visited[a] == False:
            bfs(a)
            answer += 1
    
    return answer
