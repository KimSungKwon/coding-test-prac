'''
체육복
https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

먼저 여벌 체육복이 있는 학생을 검사 -> 그 학생은 -999값을 할당해서 검사에서 제외시킴
오름차순 정렬이므로 front(앞번호)꺼를 back(뒷번호)꺼 보다 우선적으로 빌림
'''

def solution(n, lost, reserve):
    answer = n
    
    # 여벌 체육복이 있는 학생 검사
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i] = -999

    for i in range(len(lost)): # if lost[i] == 2
        if lost[i] == -999:
            continue
        front = lost[i] - 1    # front is 1
        back = lost[i] + 1     # back is 3
        if lost[i] in reserve:
            reserve.remove(lost[i])
        elif front in reserve:
            reserve.remove(front)
        elif back in reserve:
            reserve.remove(back)
        else:
            answer -= 1

    return answer
