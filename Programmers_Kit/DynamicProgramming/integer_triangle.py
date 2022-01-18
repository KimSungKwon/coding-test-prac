'''
정수 삼각형
https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3

메모이제이션은 안 쓰고 최적 부분 구조 성질 이용  Bottom up 방식

모서리부분과 안쪽부분 구분지어서 점화식 계산

triangle[i][j] = max(triangle[i-1][j-1]+triangle[i][j], triangle[i-1][j]+triangle[i][j])
'''

def solution(triangle):
    answer = 0
    length = len(triangle)

    for i in range(1, length):
        for j in range(0, len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            else:
                triangle[i][j] = max(triangle[i-1][j-1]+triangle[i][j], triangle[i-1][j]+triangle[i][j])
        print(triangle[i])

    answer = max(triangle[length-1])
    return answer
