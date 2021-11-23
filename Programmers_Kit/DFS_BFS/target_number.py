'''
타겟 넘버
https://programmers.co.kr/learn/courses/30/lessons/43165

+, - 각각 분기 트리 -> BFS
'''

from collections import deque

def solution(numbers, target):
    answer = 0
    length = len(numbers)
    q = deque()
    
    # BFS  1. 시작 노드 Queue에 삽입
    q.append([numbers[0], 0])
    q.append([-1*numbers[0], 0])

    # BFS  2. Queue가 다 빌 때 까지 반복
    while q:
        #BFS  3. pop한 값에 다음 원소를 +, -해서 나올 수 있는 값 삽입
        temp = q.popleft()
        index = temp[1] + 1

        # 아직 numbers의 모든 수를 더하거나 빼서 나온 결과가 아니면
        if index < length:
            q.append([temp[0]+numbers[index], index])
            q.append([temp[0]-numbers[index], index])

        # temp가 numbers의 마지막 수를 더하거나 빼서 나온 결과 값이면
        else:
            if temp[0] == target:
                answer += 1



    return answer
