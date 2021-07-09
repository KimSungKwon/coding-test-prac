'''
프린터
https://programmers.co.kr/learn/courses/30/lessons/42587

'''

import collections

def solution(priorities, location):
    answer = 0
    que = collections.deque()
    for i in range(len(priorities)):
      que.append((priorities[i], i))

    while(que):
      if (que[0] == max(que, key= lambda x: x[0])):
        temp = que.popleft()
        answer += 1 
        if location == temp[1]:
          return answer
      else:
        que.append(que.popleft()) 
