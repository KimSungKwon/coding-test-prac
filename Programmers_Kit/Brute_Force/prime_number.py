'''
소수 찾기
https://programmers.co.kr/learn/courses/30/lessons/42839

permutations(iter, r) : r개의 원소를 써서 순열 생성
리스트 중복 제거 : set의 특성(중복 허용 안 함) 이용
'''

import itertools

def solution(numbers):
    answer = 0
    permut = []
    for r in range(len(numbers)):
        all = list(map(''.join, itertools.permutations(numbers, r+1)))  # 순열 생성
        all = list(set(all))    # 중복 제거 (01과 01 중복)
        
        for j in range(len(all)):
            permut.append(int(all[j]))
            
    permut = list(set(permut))  # 중복 제거 (01과 1 중복)

    answer = len(permut)
    
    # 소수 아닌거 갯수에서 
    for i in range(len(permut)):
        if permut[i] == 0 or permut[i] == 1:
            answer -= 1
            
        for j in range(2, permut[i]):
            if permut[i] % j == 0:
                answer -= 1
                break
                
    return answer
