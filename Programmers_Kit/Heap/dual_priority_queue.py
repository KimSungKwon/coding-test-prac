'''
이중 우선순위 큐
https://programmers.co.kr/learn/courses/30/lessons/42628

minHeap과 maxHeap을 동시에 다루어서 최대값, 최소값을 컨트롤 하였음.
'''

import heapq

def solution(jobs):
    answer = []
    minheap = []
    maxheap = []

    for i in range(len(jobs)):
        oper = list(jobs[i].split())  # if jobs[0] == "I 16", oper = ['I', '16']
        
        if oper[0] == 'I':      # I n
            heapq.heappush(minheap, int(oper[1]))
            heapq.heappush(maxheap, -int(oper[1]))

        elif oper[1] == '1':    # D 1 : pop maximum value
            if not minheap:
                continue
            heapq.heappop(maxheap)
            minheap = list(map(lambda x: -x, maxheap)) # 부호 반대로
            heapq.heapify(minheap)  # 힙 재정렬

        elif oper[1] == '-1':   # D -1 : pop minimum value
            if not minheap:
                continue
            heapq.heappop(minheap)
            maxheap = list(map(lambda x: -x, minheap))  # 부호 반대로
            heapq.heapify(maxheap)  # 힙 재정렬

    if not minheap:
        answer = [0, 0]
    else:
        answer.append(-maxheap[0])
        answer.append(minheap[0])

    return answer
