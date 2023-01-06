'''
N으로 표현
https://school.programmers.co.kr/learn/courses/30/lessons/42895

바텀업 방식
'''

def solution(N, number):
    answer = -1

    if N == number:    # 아래 중첩 for문에는 i == 1 일 때 답인 경우를 상정하지 않아서 여기서 해결
        return 1
    
    # dp[i] = N을 i번 써서 구한 값
    # dp[1] = 5 
    # dp[2] = 5+5, 5-5, 5*5, 5%5
    # dp[3] = 5+5+5, 5+5-5, 5+5*5, ... dp[x] +-*% dp[3-x]
    # dp[i] = dp[j] +-*% dp[i-j]

    dp = [[] for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].append(int(str(N) * i))
        
    print(dp)
    # dp[i] = dp[j] +-*% dp[i-j]
    for i in range(2, 9): 
        for j in range(1, i): 
            for data1 in dp[j]:       # dp[j]
                for data2 in dp[i-j]: # dp[i-j
                    dp[i].append(data1 + data2)
                    dp[i].append(data1 - data2)
                    dp[i].append(data1 * data2)
                    if data2 != 0:
                        dp[i].append(data1 // data2)
        
        if number in dp[i]:
            answer = i
            break
            
    return answer
