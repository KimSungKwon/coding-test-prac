'''
카펫
https://programmers.co.kr/learn/courses/30/lessons/42842

brown == (가로+2)x2 + (세로)x2 를 만족하는 값을 완전탐색
'''
def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            height = i
            width = yellow // i

            if (width * 2) + ((height + 2) * 2) == brown:
                answer.append(width + 2)
                answer.append(height + 2)
                break
    
    return answer
