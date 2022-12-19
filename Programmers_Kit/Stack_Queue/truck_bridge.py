'''
다리를 지나는 트럭
https://programmers.co.kr/learn/courses/30/lessons/42583
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque()    # 다리에 있는 트럭들
    trucks = deque(truck_weights)   # 대기 중인 트럭들
    bridge_weight = 0   # 다리에 있는 트럭들의 무게
    time = 0

    while (bridge or trucks):
        time += 1
        
        if bridge and (time == bridge[0][1] + bridge_length):   # 다리에 트럭이 있고 맨 앞 트럭의 시간이 다 됐을 때
            bridge_weight -= bridge[0][0]
            bridge.popleft()
            
        if trucks and (trucks[0] + bridge_weight <= weight):    # 남아있는 트럭이 있고 다리의 무게가 여유 있을 때
            bridge_weight += trucks[0]
            bridge.append((trucks.popleft(), time))
    
    return time

