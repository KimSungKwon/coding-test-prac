'''
카펫
https://programmers.co.kr/learn/courses/30/lessons/42842

yellow 값이 24라면, 24로 만들 수 있는 사각형은 24x1, 12x2, 8x3, 6x4
각 종류마다 완전탐색.
brown == (가로+2)x2 + (세로+2)x2 를 만족해야 함.
'''

def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            quot = yellow // i  # quot: 가로  i: 세로
            if ((quot + 2) * 2) + (i * 2) == brown:  # brown == (가로+2)x2 + (세로+2)x2
                answer = [quot+2, i+2]
                return answer
