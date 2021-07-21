'''
구명보트
https://programmers.co.kr/learn/courses/30/lessons/42885

내림차 순으로 정렬. left: 최대값의 인덱스 right: 최소값의 인덱스
최대값과 최소값의 합이 limit 이하일 경우 left +1, right +1 (다음으로 큰 최대값, 다음으로 작은 최소값)
limit 초과일 경우 left만 +1 (최소값은 그대로 있고 최대값만 다음차례로)
'''

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    right = len(people) - 1
    left = 0

    while True:
        if left == right:  # 리스트에 확인할 원소가 하나만 있음
            answer += 1
            break
        elif left > right: # 리스트에 확인할 원소가 없음
            break
        elif people[left] + people[right] <= limit:
            left += 1
            right -= 1
            answer += 1
        else:
            left += 1
            answer += 1

    return answer
