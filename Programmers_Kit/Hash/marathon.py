'''
완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42576

collections의 Counter 함수를 이용해서 리스트내의 동일한 값의 멤버(동명이인) 수 파악
'''

import collections

def solution(participant, completion):
    answer = ''
    counter1 = collections.Counter(participant) 
    counter2 = collections.Counter(completion)
    for i in participant:
        if (counter1[i] - counter2[i] != 0):    # 완주자 명단에 없거나 동명이인중 나머지가 완주를 못 했으면
            answer = i
    return answer
