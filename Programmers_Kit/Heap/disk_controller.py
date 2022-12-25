'''
디스크 컨트롤러
https://school.programmers.co.kr/learn/courses/30/lessons/42627
'''
import heapq

def solution(jobs):
    answer = 0
    count, last = 0, -1    # 실행한 작업 수, 지나간 초침(?.. jobs의 pop을 대신하여 중복삽입 안하게)
    heapq.heapify(jobs)
    ready = []
    
    time = jobs[0][0]

    while count < len(jobs):
        for job in jobs:
            if last < job[0] <= time:    # last < job[0] and job[0] <= time
                heapq.heappush(ready, (job[1], job[0]))

        if ready:
            last = time    
            
            term, start = heapq.heappop(ready)
            print(term, start)
            count += 1
            time += term    
            answer += (time - start)  
            print(answer)
        else:
            time += 1
    
    return answer // len(jobs)
