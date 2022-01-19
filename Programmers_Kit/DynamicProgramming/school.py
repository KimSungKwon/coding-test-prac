'''
등굣길 
https://programmers.co.kr/learn/courses/30/lessons/42898
'''

def solution(m, n, puddles):
    # 지도 초기화
    maps = [[0] * (m+1) for _ in range(n+1)]
    # 우물의 좌표 거꾸로 
    puddles = [[y, x] for [x, y] in puddles]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1:
                maps[i][j] = 1
            elif [i, j] not in puddles:
                maps[i][j] = (maps[i-1][j]+maps[i][j-1]) % 1000000007
                
    answer = maps[i][j]
    
    return answer
