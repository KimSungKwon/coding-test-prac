'''
기능개발
https://programmers.co.kr/learn/courses/30/lessons/42586

math.ceil(x): x보다 높은 정수 값중 가장 낮은 값.  ex) math.ceil(10.1) == 11,  math.ceil(12.6) == 13
'''

import collections
import math

def solution(progresses, speeds):
    answer = []
    days = collections.deque()
    
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    while(days):
        deploy = 0
        for i in range(1, len(days)):
            if days[i] <= days[0]:
                deploy += 1
            else:
                break
        for j in range(deploy+1):
            days.popleft()
      
        answer.append(deploy+1)
    return answer
