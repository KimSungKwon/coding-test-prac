'''
도둑질
https://school.programmers.co.kr/learn/courses/30/lessons/42897

coding-test-prac/Chapter08_DP/8-6.py 와 유사
'''

def solution(money):
    answer = 0
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    
    # dp1: 첫 번째 털고 마지막 안 털고
    dp1[0] = money[0]
    for i in range(1, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    
    # dp2: 첫 번째 안 털고 마지막 털고
    dp2[0] = 0
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
        
    # dp1과 dp2 중 더 큰 값
    answer = max(dp1[-2], dp2[-1])
    
    return answer
