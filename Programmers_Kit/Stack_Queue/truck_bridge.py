'''
다리를 지나는 트럭
https://programmers.co.kr/learn/courses/30/lessons/42583
'''

import collections

def solution(bridge_length, weight, truck_weights):
    bridge = 0  # bridge: 현재 다리에 놓여진 무게
    bridge_que = collections.deque()    # 현재 다리에 있는 트럭들 (트럭무게, 진입시간)
    truck_que = collections.deque(truck_weights)  # 현재 대기중인 트럭들
    time = 0

    while(bridge_que or truck_que):
        time += 1

        if bridge_que and (bridge_que[0][1] + bridge_length == time): # 트럭이 지나갈 수 있는 시간이 충족되면
            bridge -= bridge_que[0][0]
            bridge_que.popleft()
      
        if truck_que and (bridge + truck_que[0] <= weight): # 트럭이 다리에 진입해도 다리의 무게제한이 초과하지 않으면
            bridge += truck_que[0]
            bridge_que.append((truck_que.popleft(), time))

    return time
