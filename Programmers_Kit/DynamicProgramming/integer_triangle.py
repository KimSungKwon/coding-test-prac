'''
정수 삼각형
https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3

메모이제이션은 안 쓰고 최적 부분 구조 성질 이용  Bottom up 방식
'''

def solution(triangle):

    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    answer = max(triangle[-1])

    return answer
