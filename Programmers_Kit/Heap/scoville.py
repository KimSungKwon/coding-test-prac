'''
더 맵게
https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3

push, pop 할 때마다 자동으로 정렬되는 heap이용. 
while의 판단문을 min함수를 써서 했더니 시간 초과됐다.
최소값이 K보다 작은지만 확인하면 되기 때문에 scoville[0]으로 변경했더니 통과
'''

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:    # while min(scoville) < K  => (time over)
        if (len(scoville)) <= 1:
            answer = -1
            break
        temp1 = heapq.heappop(scoville)
        temp2 = heapq.heappop(scoville)
        mix = temp1 + (temp2 * 2)
        heapq.heappush(scoville, mix)
        answer += 1

    return answer
